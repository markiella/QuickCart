from .models import Cart

def get_or_create_cart(request):
    """Get or create cart for authenticated user or anonymous session"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Merge session cart with user cart if exists
        if hasattr(request, 'session') and request.session.session_key:
            try:
                session_cart = Cart.objects.get(session_key=request.session.session_key)
                # Merge items from session cart to user cart
                for item in session_cart.items.all():
                    user_item, created = cart.items.get_or_create(
                        product=item.product,
                        defaults={'quantity': item.quantity}
                    )
                    if not created:
                        user_item.quantity += item.quantity
                        user_item.save()
                
                # Delete session cart after merging
                session_cart.delete()
            except Cart.DoesNotExist:
                pass
    else:
        # For anonymous users, use session
        if not request.session.session_key:
            request.session.create()
        
        cart, created = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )
    
    return cart
