from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Product
from .utils import get_or_create_cart

def cart_detail(request):
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        messages.error(request, 'Invalid quantity.')
        return redirect('store:product_detail', slug=product.slug)
    
    if quantity > product.stock_quantity:
        messages.error(request, f'Only {product.stock_quantity} items available in stock.')
        return redirect('store:product_detail', slug=product.slug)
    
    cart = get_or_create_cart(request)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        new_quantity = cart_item.quantity + quantity
        if new_quantity > product.stock_quantity:
            messages.error(request, f'Cannot add more items. Only {product.stock_quantity} available.')
            return redirect('store:product_detail', slug=product.slug)
        cart_item.quantity = new_quantity
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_total_items': cart.get_total_items(),
            'message': f'{product.name} added to cart.'
        })
    
    return redirect('cart:cart_detail')

@require_POST
def update_cart_item(request, item_id):
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        cart_item.delete()
        messages.success(request, f'{cart_item.product.name} removed from cart.')
    elif quantity > cart_item.product.stock_quantity:
        messages.error(request, f'Only {cart_item.product.stock_quantity} items available.')
    else:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Cart updated successfully.')
    
    return redirect('cart:cart_detail')

@require_POST
def remove_from_cart(request, item_id):
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    product_name = cart_item.product.name
    cart_item.delete()
    
    messages.success(request, f'{product_name} removed from cart.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_total_items': cart.get_total_items(),
            'cart_total_price': float(cart.get_total_price()),
            'message': f'{product_name} removed from cart.'
        })
    
    return redirect('cart:cart_detail')

def clear_cart(request):
    cart = get_or_create_cart(request)
    cart.clear()
    messages.success(request, 'Cart cleared successfully.')
    return redirect('cart:cart_detail')
