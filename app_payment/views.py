from django.shortcuts import get_object_or_404, redirect , render
from django.contrib.auth.decorators import login_required
from app_payment.models import Basket, BasketItem
from app_didikala.models import Product , Color

@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user)

    color_id = request.POST.get('color')
    color = None
    if color_id:
        color = get_object_or_404(Color, id=color_id)

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product, color=color)
    
    if not created:
        basket_item.count += 1 
    else:
        basket_item.count = 1 
        

    basket_item.save()
    return redirect('cart')

@login_required
def view_basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    if not items.exists():
        return render(request, 'cart-empty.html')
    
    total_price = sum(item.product.price * item.count for item in items)
    total_price_without_discount = sum(round(item.product.price/(1-(item.product.discount/100)))*item.count for item in items)
    total_discount_price = sum(round((item.product.price/(1 - (item.product.discount/100))) - item.product.price)*item.count for item in items)
    

    return render(request, 'cart.html', {'items': items,
                                        'total_price': total_price,
                                        'total_price_without_discount' : total_price_without_discount,
                                        'total_discount_price' : total_discount_price})

def remove_from_cart(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    item.delete()
    return redirect('cart')

def update_item_count(request, item_id, action):
    item = BasketItem.objects.get(id=item_id)

    if action == 'plus':
        item.count += 1
    elif action == 'minus' and item.count > 1:
        item.count -= 1
    
    item.save()

    return redirect('cart') 


def shopping_payement(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    if not items.exists():
        return render(request, 'cart-empty.html')
    
    total_price = sum(item.product.price * item.count for item in items)
    total_price_without_discount = sum(round(item.product.price/(1-(item.product.discount/100)))*item.count for item in items)
    total_discount_price = sum(round((item.product.price/(1 - (item.product.discount/100))) - item.product.price)*item.count for item in items)
    

    return render(request, 'shopping-peyment.html', {'items': items,
                                        'total_price': total_price,
                                        'total_price_without_discount' : total_price_without_discount,
                                        'total_discount_price' : total_discount_price})

def shopping_completed(request):
    return render(request , 'shopping-complete-buy.html')

def shopping(request):
    return render(request , 'shopping.html')

def shopping_notcompleted(request):
    return render(request , 'shopping-no-complete-buy.html')