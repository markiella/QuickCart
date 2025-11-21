from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q
from django.utils import timezone
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from orders.models import Order, OrderItem
from store.models import Product, Category
from accounts.models import User
from discounts.models import DiscountUsage

@login_required
def dashboard_home(request):
    """Main dashboard view for admin, staff, and riders"""
    # Redirect customers to their order list
    if request.user.role == 'customer':
        return redirect('orders:order_list')
    
    if request.user.role not in ['admin', 'staff', 'rider']:
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    # Date range for analytics (last 30 days)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    # Filter orders based on user role
    if request.user.role == 'admin':
        orders_queryset = Order.objects.all()
    elif request.user.role in ['staff', 'rider']:
        # Staff and riders only see orders assigned to them
        orders_queryset = Order.objects.filter(assigned_staff=request.user)
    else:
        orders_queryset = Order.objects.none()
    
    # Basic statistics
    total_orders = orders_queryset.count()
    total_revenue = orders_queryset.filter(status='delivered').aggregate(
        total=Sum('total_amount')
    )['total'] or 0
    
    pending_orders = orders_queryset.filter(status='pending').count()
    total_customers = User.objects.filter(role='customer').count()
    
    # Recent orders
    recent_orders = orders_queryset.order_by('-created_at')[:10]
    
    # Top selling products (last 30 days)
    top_products = OrderItem.objects.filter(
        order__created_at__gte=start_date,
        order__status='delivered'
    ).values('product__name').annotate(
        total_sold=Sum('quantity'),
        total_revenue=Sum('total_price')
    ).order_by('-total_sold')[:5]
    
    # Monthly revenue chart data
    monthly_revenue = []
    for i in range(12):
        month_start = (end_date - timedelta(days=30*i)).replace(day=1)
        month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        
        revenue = Order.objects.filter(
            status='delivered',
            created_at__gte=month_start,
            created_at__lte=month_end
        ).aggregate(total=Sum('total_amount'))['total'] or 0
        
        monthly_revenue.append({
            'month': month_start.strftime('%b %Y'),
            'revenue': float(revenue)
        })
    
    monthly_revenue.reverse()
    
    # Low stock products
    low_stock_products = Product.objects.filter(
        stock_quantity__lte=5,
        is_available=True
    ).order_by('stock_quantity')[:10]
    
    # Get unread notifications for riders
    unread_notifications = []
    if request.user.role == 'rider':
        try:
            from notifications.models import Notification
            unread_notifications = Notification.objects.filter(
                user=request.user,
                is_read=False
            ).order_by('-created_at')
            # Clear the session flag
            if 'show_login_notifications' in request.session:
                del request.session['show_login_notifications']
        except ImportError:
            pass
    
    context = {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'total_customers': total_customers,
        'recent_orders': recent_orders,
        'top_products': top_products,
        'monthly_revenue': monthly_revenue,
        'low_stock_products': low_stock_products,
        'unread_notifications': unread_notifications,
    }
    
    # Use different templates based on user role
    if request.user.role == 'admin':
        return render(request, 'dashboard/admin_dashboard.html', context)
    elif request.user.role == 'staff':
        return render(request, 'dashboard/staff_dashboard.html', context)
    else:  # rider
        return render(request, 'dashboard/rider_dashboard.html', context)

@login_required
def analytics_view(request):
    """Detailed analytics view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    # Date range filter
    days = int(request.GET.get('days', 30))
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)
    
    # Order statistics
    orders_in_period = Order.objects.filter(created_at__gte=start_date)
    
    order_stats = {
        'total_orders': orders_in_period.count(),
        'completed_orders': orders_in_period.filter(status='delivered').count(),
        'cancelled_orders': orders_in_period.filter(status='cancelled').count(),
        'pending_orders': orders_in_period.filter(status='pending').count(),
        'total_revenue': orders_in_period.filter(status='delivered').aggregate(
            total=Sum('total_amount')
        )['total'] or 0,
    }
    
    # Customer statistics
    new_customers = User.objects.filter(
        role='customer',
        date_joined__gte=start_date
    ).count()
    
    repeat_customers = User.objects.filter(
        role='customer',
        total_orders__gt=1
    ).count()
    
    # Category performance
    category_performance = OrderItem.objects.filter(
        order__created_at__gte=start_date,
        order__status='delivered'
    ).values('product__category__name').annotate(
        total_sold=Sum('quantity'),
        total_revenue=Sum('total_price')
    ).order_by('-total_revenue')
    
    # Discount usage
    discount_usage = DiscountUsage.objects.filter(
        used_at__gte=start_date
    ).values('discount_type').annotate(
        usage_count=Count('id'),
        total_discount=Sum('discount_amount')
    )
    
    context = {
        'days': days,
        'order_stats': order_stats,
        'new_customers': new_customers,
        'repeat_customers': repeat_customers,
        'category_performance': category_performance,
        'discount_usage': discount_usage,
    }
    
    return render(request, 'dashboard/analytics.html', context)

@login_required
def inventory_management(request):
    """Inventory management view - Admin can add products, Staff can only update stock"""
    if request.user.role not in ['admin', 'staff']:
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    # Filter products
    category_filter = request.GET.get('category')
    stock_filter = request.GET.get('stock')
    search_query = request.GET.get('search')
    
    products = Product.objects.all()
    
    if category_filter:
        products = products.filter(category__slug=category_filter)
    
    if stock_filter == 'low':
        products = products.filter(stock_quantity__lte=5)
    elif stock_filter == 'out':
        products = products.filter(stock_quantity=0)
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Order by newest first (FIFO - First In First Out means newest products first)
    products = products.order_by('-created_at', 'name')
    categories = Category.objects.filter(is_active=True)
    
    # Product statistics
    total_products = Product.objects.count()
    available_products = Product.objects.filter(is_available=True).count()
    low_stock = Product.objects.filter(stock_quantity__lte=5).count()
    out_of_stock = Product.objects.filter(stock_quantity=0).count()
    
    context = {
        'products': products,
        'categories': categories,
        'category_filter': category_filter,
        'stock_filter': stock_filter,
        'search_query': search_query,
        'total_products': total_products,
        'available_products': available_products,
        'low_stock': low_stock,
        'out_of_stock': out_of_stock,
    }
    
    return render(request, 'dashboard/inventory.html', context)

@login_required
def update_stock(request, product_id):
    """Update product stock"""
    if request.user.role not in ['admin', 'staff']:
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        new_stock = request.POST.get('stock_quantity')
        try:
            new_stock = int(new_stock)
            if new_stock >= 0:
                product.stock_quantity = new_stock
                product.save()
                messages.success(request, f'Stock updated for {product.name}')
            else:
                messages.error(request, 'Stock quantity cannot be negative.')
        except ValueError:
            messages.error(request, 'Invalid stock quantity.')
    
    return redirect('dashboard:inventory')

@login_required
def user_management(request):
    """User management view for admin"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    users = User.objects.all().order_by('-created_at')
    
    context = {
        'users': users,
    }
    return render(request, 'dashboard/user_management.html', context)

@login_required
def product_management(request):
    """Product management view for admin"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.filter(is_active=True)
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'dashboard/product_management.html', context)

@login_required
def category_management(request):
    """Category management view for admin"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    categories = Category.objects.all().order_by('name')
    
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/category_management.html', context)

@login_required
def get_order_details(request, order_id):
    """Get order details via AJAX for modal display"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    try:
        order = Order.objects.get(id=order_id)
        
        # Get order items
        items = order.items.all()
        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'price': str(item.product_price),
                'quantity': item.quantity,
                'total': str(item.total_price),
            })
        
        # Get rider list (delivery staff)
        rider_users = User.objects.filter(role='rider').order_by('first_name')
        staff_list = [{'id': str(rider.id), 'name': rider.get_full_name()} for rider in rider_users]
        
        return JsonResponse({
            'order_number': order.order_number,
            'status': order.get_status_display(),
            'status_code': order.status,
            'customer_name': order.customer_name,
            'customer_email': order.user.email,
            'customer_phone': order.customer_phone,
            'customer_type': order.user.get_role_display(),
            'delivery_address': order.delivery_address,
            'subtotal': str(order.subtotal),
            'discount_amount': str(order.discount_amount),
            'delivery_fee': str(order.delivery_fee),
            'total_amount': str(order.total_amount),
            'created_at': order.created_at.strftime('%b %d, %Y - %I:%M %p'),
            'assigned_staff': order.assigned_staff.get_full_name() if order.assigned_staff else 'Unassigned',
            'assigned_staff_id': str(order.assigned_staff.id) if order.assigned_staff else None,
            'staff_list': staff_list,
            'items': items_data,
        })
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def update_order_status(request, order_id):
    """Update order status via AJAX"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        import json
        data = json.loads(request.body)
        status = data.get('status')
        
        order = Order.objects.get(id=order_id)
        order.status = status
        order.save()
        
        # Create status history
        from orders.models import OrderStatusHistory
        OrderStatusHistory.objects.create(
            order=order,
            status=status,
            changed_by=request.user,
            notes=f'Status changed to {order.get_status_display()}'
        )
        
        return JsonResponse({'success': True})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def assign_staff(request, order_id):
    """Assign rider to order via AJAX"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        import json
        data = json.loads(request.body)
        rider_id = data.get('staff_id')
        
        order = Order.objects.get(id=order_id)
        
        if rider_id:
            rider = User.objects.get(id=rider_id, role='rider')
            order.assigned_staff = rider
        else:
            order.assigned_staff = None
        
        order.save()
        
        return JsonResponse({'success': True})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Rider not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def admin_orders(request):
    """Admin orders management view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('store:product_list')
    
    # Filter orders
    status_filter = request.GET.get('status')
    
    orders = Order.objects.all().order_by('-created_at')
    
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    # Pagination
    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    status_choices = Order.STATUS_CHOICES
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'status_choices': status_choices,
    }
    
    return render(request, 'dashboard/admin_orders.html', context)

@login_required
def promo_management(request):
    """Promo code management view for admin"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    from discounts.models import PromoCode
    promos = PromoCode.objects.all().order_by('-created_at')
    
    context = {
        'promos': promos,
    }
    return render(request, 'dashboard/promo_management.html', context)

@login_required
def add_product(request):
    """Add new product via AJAX"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    if request.method == 'POST':
        try:
            from store.models import Product, Category
            
            category = Category.objects.get(id=request.POST.get('category_id'))
            
            from django.utils.text import slugify
            
            name = request.POST.get('name')
            slug = slugify(name)
            
            # Ensure unique slug
            counter = 1
            original_slug = slug
            while Product.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            product = Product.objects.create(
                name=name,
                slug=slug,
                description=request.POST.get('description', ''),
                price=float(request.POST.get('price')),
                stock_quantity=int(request.POST.get('stock_quantity')),
                unit=request.POST.get('unit'),
                category=category,
                is_available=True
            )
            
            # Handle image upload if provided
            if 'image' in request.FILES:
                product.image = request.FILES['image']
                product.save()
            
            return JsonResponse({'success': True, 'product_id': product.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def get_product(request, product_id):
    """Get product data for editing and viewing"""
    if request.user.role not in ['admin', 'staff']:
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    try:
        from store.models import Product
        product = Product.objects.get(id=product_id)
        
        image_url = product.image.url if product.image else None
        
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'stock_quantity': product.stock_quantity,
            'unit': product.unit,
            'category_id': product.category.id,
            'category_name': product.category.name,
            'image_url': image_url,
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

@login_required
def edit_product(request, product_id):
    """Edit product via AJAX"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    if request.method == 'POST':
        try:
            from store.models import Product, Category
            
            product = Product.objects.get(id=product_id)
            category = Category.objects.get(id=request.POST.get('category_id'))
            
            from django.utils.text import slugify
            
            name = request.POST.get('name')
            
            # Update slug if name changed or slug is missing
            if product.name != name or not product.slug:
                slug = slugify(name)
                counter = 1
                original_slug = slug
                while Product.objects.filter(slug=slug).exclude(id=product_id).exists():
                    slug = f"{original_slug}-{counter}"
                    counter += 1
                product.slug = slug
            
            product.name = name
            product.description = request.POST.get('description', '')
            product.price = float(request.POST.get('price'))
            product.stock_quantity = int(request.POST.get('stock_quantity'))
            product.unit = request.POST.get('unit')
            product.category = category
            
            # Handle image upload if provided
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            
            product.save()
            
            return JsonResponse({'success': True})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def delete_product(request, product_id):
    """Delete product via AJAX"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    if request.method == 'DELETE':
        try:
            from store.models import Product
            product = Product.objects.get(id=product_id)
            product.delete()
            
            return JsonResponse({'success': True})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def user_management(request):
    """User management view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    # Get all users
    users = User.objects.all().order_by('-date_joined')
    
    # User statistics
    total_users = User.objects.count()
    customers = User.objects.filter(role='customer').count()
    riders = User.objects.filter(role='rider').count()
    admins = User.objects.filter(role='admin').count()
    
    context = {
        'users': users,
        'total_users': total_users,
        'customers': customers,
        'riders': riders,
        'admins': admins,
    }
    
    return render(request, 'dashboard/user_management.html', context)

@login_required
def product_management(request):
    """Product management view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    # Get all products
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    # Product statistics
    total_products = Product.objects.count()
    available_products = Product.objects.filter(is_available=True).count()
    low_stock = Product.objects.filter(stock_quantity__lte=5).count()
    
    context = {
        'products': products,
        'total_products': total_products,
        'available_products': available_products,
        'low_stock': low_stock,
        'categories': categories,
    }
    
    return render(request, 'dashboard/product_management.html', context)

@login_required
def category_management(request):
    """Category management view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    # Get all categories
    categories = Category.objects.annotate(
        product_count=Count('products')
    ).order_by('name')
    
    # Category statistics
    total_products = Product.objects.count()
    
    context = {
        'categories': categories,
        'total_products': total_products,
    }
    
    return render(request, 'dashboard/category_management.html', context)

@login_required
def promo_management(request):
    """Promo codes management view"""
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard:home')
    
    from discounts.models import PromoCode
    
    # Get all promo codes
    promos = PromoCode.objects.all().order_by('-created_at')
    
    # Promo statistics
    total_promos = PromoCode.objects.count()
    active_promos = PromoCode.objects.filter(is_active=True).count()
    
    context = {
        'promos': promos,
        'total_promos': total_promos,
        'active_promos': active_promos,
    }
    
    return render(request, 'dashboard/promo_management.html', context)
