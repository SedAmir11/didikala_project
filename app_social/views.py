from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from app_didikala.models import Product , ProductDetail
from .models import Comment , Advantage , Disadvantage
from app_payment.models import Order

@login_required
def comment_page(request, product_id):
    context = {}
    product = get_object_or_404(Product, id=product_id)
    product_detail = get_object_or_404(ProductDetail, product=product)
    context['product'] = product
    context['product_detail'] = product_detail

    user_orders = Order.objects.filter(user=request.user)
    has_ordered_product = user_orders.filter(items__product=product).exists()

    if not has_ordered_product:
        return redirect('product_page', id=product.id)

    existing_comment = Comment.objects.filter(product=product, user=request.user).first()

    if request.method == 'POST':
        title = request.POST.get('title') 
        description = request.POST.get('description')  
        advantages = request.POST.getlist('comment[advantages][]') 
        disadvantages = request.POST.getlist('comment[disadvantages][]') 
        suggest = request.POST.get('suggest')

        comment = Comment.objects.create(
            user=request.user,
            product=product,
            title=title,
            description=description,
            suggest=suggest 
        )

        for advantage_text in advantages:
            advantage, created = Advantage.objects.get_or_create(text=advantage_text)
            comment.advantages.add(advantage)

        for disadvantage_text in disadvantages:
            disadvantage, created = Disadvantage.objects.get_or_create(text=disadvantage_text)
            comment.disadvantages.add(disadvantage)

        comment.save()

        return redirect('product_page', id=product.id)


    if existing_comment:
        return redirect('product_page', id=product.id)

    return render(request, 'product-comment.html', context)
