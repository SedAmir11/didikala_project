from django.shortcuts import get_object_or_404, redirect , render
from django.contrib.auth.decorators import login_required
from app_payment.models import Basket, BasketItem , OrderItem , Order , Transaction
from app_didikala.models import Product , Color 
from app_account.models import Address

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
    context = {}
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    if not items.exists():
        return render(request, 'cart-empty.html')
    
    context['total_price'] = sum(item.product.price * item.count for item in items)
    context['total_price_without_discount'] = sum(round(item.product.price/(1-(item.product.discount/100)))*item.count for item in items)
    context['total_discount_price'] = sum(round((item.product.price/(1 - (item.product.discount/100))) - item.product.price)*item.count for item in items)
    context['items'] = items   

    return render(request, 'cart.html', context)

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
    context = {}
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    if not items.exists():
        return render(request, 'cart-empty.html')
    
    context['total_price'] = sum(item.product.price * item.count for item in items)
    context['total_price_without_discount'] = sum(round(item.product.price/(1-(item.product.discount/100)))*item.count for item in items)
    context['total_discount_price'] = sum(round((item.product.price/(1 - (item.product.discount/100))) - item.product.price)*item.count for item in items)
    context['items'] = items

    return render(request, 'shopping-peyment.html', context)

def shopping_completed(request):
    return render(request , 'shopping-complete-buy.html')

def shopping(request):
    context = {}
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    context['addresses'] = Address.objects.filter(user=request.user)
    context['default_address'] = context['addresses'].first() if context['addresses'] else None

    context['total_price'] = sum(item.product.price * item.count for item in items)
    context['total_price_without_discount'] = sum(round(item.product.price/(1-(item.product.discount/100)))*item.count for item in items)
    context['total_discount_price'] = sum(round((item.product.price/(1 - (item.product.discount/100))) - item.product.price)*item.count for item in items)
    context['items'] = items

    return render(request, 'shopping.html', context)

def shopping_notcompleted(request):
    return render(request , 'shopping-no-complete-buy.html')

@login_required
def finalize_order(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = BasketItem.objects.filter(basket=basket)

    total_price = sum(item.product.price * item.count for item in items)


    transaction = Transaction.objects.create(
        status=True, 
        ref_code="سفارشی-" + str(request.user.id),
        price=total_price 
    )

    order = Order.objects.create(user=request.user, transaction=transaction)

    for item in items:
        OrderItem.objects.create(order=order, product=item.product, count=item.count , color = item.color)

        item.product.count -= item.count 
        item.product.save()

    basket.items.all().delete()

    return redirect(shopping_completed)