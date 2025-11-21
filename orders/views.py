from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model
from cart.utils import get_or_create_cart
from discounts.utils import calculate_discount
from .models import Order, OrderItem, OrderStatusHistory
from .forms import CheckoutForm, OrderStatusForm

User = get_user_model()

@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')
    
    # Check stock availability
    for item in cart.items.all():
        if item.quantity > item.product.stock_quantity:
            messages.error(request, f'Insufficient stock for {item.product.name}. Only {item.product.stock_quantity} available.')
            return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST, user=request.user)
        if form.is_valid():
            with transaction.atomic():
                # Calculate totals
                subtotal = cart.get_total_price()
                
                # Calculate discount
                discount_info = calculate_discount(request.user, subtotal)
                discount_amount = discount_info['amount']
                
                # Delivery is free as per requirements
                delivery_fee = 0
                total_amount = subtotal - discount_amount + delivery_fee
                
                # Create order
                order = form.save(commit=False)
                order.user = request.user
                order.subtotal = subtotal
                order.discount_amount = discount_amount
                order.delivery_fee = delivery_fee
                order.total_amount = total_amount
                order.discount_type = discount_info['type']
                order.discount_code = discount_info.get('code', '')
                order.save()
                
                # Create order items and update stock
                for cart_item in cart.items.all():
                    OrderItem.objects.create(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity
                    )
                    
                    # Update product stock
                    product = cart_item.product
                    product.stock_quantity -= cart_item.quantity
                    product.save()
                
                # Update user stats
                user = request.user
                user.total_orders += 1
                if user.is_first_time_customer:
                    user.is_first_time_customer = False
                user.save()
                
                # Create status history
                OrderStatusHistory.objects.create(
                    order=order,
                    status='pending',
                    changed_by=request.user,
                    notes='Order placed'
                )
                
                # Create notification for admins
                try:
                    from notifications.models import Notification
                    admin_users = User.objects.filter(role='admin')
                    for admin in admin_users:
                        Notification.objects.create(
                            user=admin,
                            notification_type='new_order',
                            title='🛒 New Order Received',
                            message=f'Customer {request.user.get_full_name or request.user.username} placed order {order.order_number} for ₱{order.total_amount}',
                            order_id=str(order.id)
                        )
                except ImportError:
                    pass  # Notifications app not available
                
                # Clear cart
                cart.clear()
                
                messages.success(request, f'Order {order.order_number} placed successfully!')
                return redirect('orders:order_detail', order_id=order.id)
    else:
        form = CheckoutForm(user=request.user)
    
    # Calculate discount for display
    subtotal = cart.get_total_price()
    discount_info = calculate_discount(request.user, subtotal)
    
    context = {
        'form': form,
        'cart': cart,
        'subtotal': subtotal,
        'discount_info': discount_info,
        'delivery_fee': 0,
        'total': subtotal - discount_info['amount'],
    }
    
    return render(request, 'orders/checkout.html', context)

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    
    return render(request, 'orders/order_detail.html', context)

# Staff/Admin/Rider views
@login_required
def staff_order_list(request):
    if request.user.role not in ['staff', 'admin', 'rider']:
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    orders = Order.objects.all()
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    # Filter by assigned staff/rider (for staff and rider users)
    if request.user.role == 'staff':
        orders = orders.filter(assigned_staff=request.user)
    elif request.user.role == 'rider':
        orders = orders.filter(assigned_staff=request.user)
    
    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'status_choices': Order.STATUS_CHOICES,
    }
    
    return render(request, 'orders/staff_order_list.html', context)

@login_required
def staff_order_detail(request, order_id):
    if request.user.role not in ['staff', 'admin', 'rider']:
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order, user=request.user)
        if form.is_valid():
            old_status = order.status
            old_assigned_staff = order.assigned_staff
            order = form.save()
            
            # Create status history if status changed
            if old_status != order.status:
                OrderStatusHistory.objects.create(
                    order=order,
                    status=order.status,
                    changed_by=request.user,
                    notes=f'Status changed from {old_status} to {order.status}'
                )
                
                # Update delivered_at timestamp
                if order.status == 'delivered':
                    order.delivered_at = timezone.now()
                    order.save()
            
            # Create notification if rider was assigned
            if old_assigned_staff != order.assigned_staff and order.assigned_staff:
                try:
                    from notifications.models import Notification
                    # Get order items for the message
                    items = order.items.all()
                    items_str = ', '.join([f"{item.quantity}x {item.product_name}" for item in items])
                    
                    Notification.objects.create(
                        user=order.assigned_staff,
                        notification_type='rider_assigned',
                        title='🚚 New Delivery Assignment',
                        message=f'You have been assigned to deliver order {order.order_number} ({items_str}) to {order.customer_name}',
                        order_id=str(order.id)
                    )
                except ImportError:
                    pass  # Notifications app not available
            
            messages.success(request, 'Order updated successfully.')
            return redirect('orders:staff_order_detail', order_id=order.id)
    else:
        form = OrderStatusForm(instance=order, user=request.user)
    
    context = {
        'order': order,
        'form': form,
    }
    
    return render(request, 'orders/staff_order_detail.html', context)
