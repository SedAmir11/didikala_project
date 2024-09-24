from app_payment.models import Basket, BasketItem

def cart_items(request):
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
        items = BasketItem.objects.filter(basket=basket)
        total_price = sum(item.product.price * item.count for item in items)
        return {'cart_items': items,
                'sum_price' : total_price}
    return {'cart_items': []}
