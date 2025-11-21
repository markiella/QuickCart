from decimal import Decimal
from .models import SukiDiscount, FirstTimeCustomerPromo, PromoCode, DiscountUsage

def calculate_discount(user, order_amount, promo_code=None):
    """
    Calculate the best available discount for a user
    Returns a dictionary with discount information
    """
    discount_info = {
        'type': 'none',
        'amount': Decimal('0.00'),
        'description': '',
        'code': ''
    }
    
    available_discounts = []
    
    # Check promo code discount
    if promo_code:
        try:
            promo = PromoCode.objects.get(code=promo_code.upper(), is_active=True)
            if promo.is_valid():
                promo_discount = promo.calculate_discount(order_amount)
                if promo_discount > 0:
                    available_discounts.append({
                        'type': 'promo_code',
                        'amount': promo_discount,
                        'description': f'Promo Code: {promo.code}',
                        'code': promo.code,
                        'priority': 1
                    })
        except PromoCode.DoesNotExist:
            pass
    
    # Check first-time customer discount
    if user.is_authenticated and user.is_first_time_customer:
        try:
            first_time_promo = FirstTimeCustomerPromo.objects.filter(is_active=True).first()
            if first_time_promo and first_time_promo.is_valid():
                first_time_discount = first_time_promo.calculate_discount(order_amount)
                if first_time_discount > 0:
                    available_discounts.append({
                        'type': 'first_time',
                        'amount': first_time_discount,
                        'description': f'First-time Customer: {first_time_promo.name}',
                        'code': '',
                        'priority': 2
                    })
        except FirstTimeCustomerPromo.DoesNotExist:
            pass
    
    # Check Suki discount
    if user.is_authenticated and user.total_orders >= 3:
        try:
            # Get the highest applicable suki discount
            suki_discount = SukiDiscount.objects.filter(
                minimum_orders__lte=user.total_orders,
                is_active=True
            ).order_by('-discount_percentage').first()
            
            if suki_discount:
                suki_amount = order_amount * (suki_discount.discount_percentage / 100)
                available_discounts.append({
                    'type': 'suki',
                    'amount': suki_amount,
                    'description': f'Suki Discount: {suki_discount.discount_percentage}%',
                    'code': '',
                    'priority': 3
                })
        except SukiDiscount.DoesNotExist:
            pass
    
    # Select the best discount (highest amount, then by priority)
    if available_discounts:
        best_discount = max(available_discounts, key=lambda x: (x['amount'], -x['priority']))
        discount_info = best_discount
    
    return discount_info

def apply_discount(user, order_amount, discount_info):
    """
    Apply and record discount usage
    """
    if discount_info['amount'] > 0:
        # Record discount usage
        promo_code_obj = None
        if discount_info['type'] == 'promo_code':
            try:
                promo_code_obj = PromoCode.objects.get(code=discount_info['code'])
                promo_code_obj.usage_count += 1
                promo_code_obj.save()
            except PromoCode.DoesNotExist:
                pass
        
        DiscountUsage.objects.create(
            user=user,
            promo_code=promo_code_obj,
            discount_type=discount_info['type'],
            discount_amount=discount_info['amount'],
            order_amount=order_amount
        )
    
    return discount_info['amount']

def get_available_discounts_for_user(user, order_amount):
    """
    Get all available discounts for a user (for display purposes)
    """
    discounts = []
    
    # First-time customer discount
    if user.is_authenticated and user.is_first_time_customer:
        try:
            first_time_promo = FirstTimeCustomerPromo.objects.filter(is_active=True).first()
            if first_time_promo and first_time_promo.is_valid():
                discount_amount = first_time_promo.calculate_discount(order_amount)
                if discount_amount > 0:
                    discounts.append({
                        'type': 'first_time',
                        'name': first_time_promo.name,
                        'amount': discount_amount,
                        'description': f'Welcome discount for new customers'
                    })
        except FirstTimeCustomerPromo.DoesNotExist:
            pass
    
    # Suki discount
    if user.is_authenticated and user.total_orders >= 3:
        try:
            suki_discount = SukiDiscount.objects.filter(
                minimum_orders__lte=user.total_orders,
                is_active=True
            ).order_by('-discount_percentage').first()
            
            if suki_discount:
                discount_amount = order_amount * (suki_discount.discount_percentage / 100)
                discounts.append({
                    'type': 'suki',
                    'name': suki_discount.name,
                    'amount': discount_amount,
                    'description': f'Loyal customer discount - {suki_discount.discount_percentage}%'
                })
        except SukiDiscount.DoesNotExist:
            pass
    
    return discounts
