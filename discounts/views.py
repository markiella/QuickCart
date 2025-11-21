from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from cart.utils import get_or_create_cart
from .utils import calculate_discount
from .models import PromoCode

@require_POST
@login_required
def apply_promo_code(request):
    """AJAX view to apply promo code"""
    promo_code = request.POST.get('promo_code', '').strip().upper()
    
    if not promo_code:
        return JsonResponse({
            'success': False,
            'message': 'Please enter a promo code.'
        })
    
    cart = get_or_create_cart(request)
    order_amount = cart.get_total_price()
    
    # Calculate discount with promo code
    discount_info = calculate_discount(request.user, order_amount, promo_code)
    
    if discount_info['type'] == 'promo_code':
        return JsonResponse({
            'success': True,
            'discount_amount': float(discount_info['amount']),
            'discount_description': discount_info['description'],
            'new_total': float(order_amount - discount_info['amount']),
            'message': f'Promo code applied! You saved ₱{discount_info["amount"]:.2f}'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Invalid or expired promo code.'
        })

def promo_code_list(request):
    """Display active promo codes (for marketing purposes)"""
    active_promos = PromoCode.objects.filter(is_active=True)
    
    context = {
        'promos': active_promos,
    }
    
    return render(request, 'discounts/promo_list.html', context)
