from .models import Cart, CartItem
from .views import cartId

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(card_id = cartId(request))

        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)