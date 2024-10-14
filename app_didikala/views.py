from django.shortcuts import render , get_object_or_404 , redirect
from app_didikala.models import Brand,division ,Product ,banner ,image , Category , ProductDetail , Favorite
from django.contrib.auth.decorators import login_required
from app_account.models import UserProfile
from app_social.models import Comment
from django.db.models import Q

def index(request):
    categories = Category.objects.filter(division_id = 1)
    context = {
        'banner_images' : banner.objects.get(title='home-main').images,
        'clothes_product' : Product.objects.filter(categories__in=Category.objects.filter(division_id = 1)).distinct(),
        'digital_product' : Product.objects.filter(categories__in=Category.objects.filter(division_id = 2)).distinct()
    }
    return render(request , 'index.html' , context)

def notfoundpage(request):
    return render(request , '404.html' , status=404)

def blog(request):
    return render(request , 'blog.html')


def cart_empty_next_list(request):
    return render(request , 'cart-empty-next-list.html')

def index2(request):
    return render(request , 'index-2.html')

def page_faq(request):
    return render(request , 'page-faq.html')

def page_faq_category(request):
    return render(request , 'page-faq-category.html')

def page_faq_question(request):
    return render(request , 'page-faq-question.html')

def verify_phone(request):
    return render(request , 'verify-phone-number.html')

def page_privacy(request):
    return render(request , 'page-privacy.html')

def single_blog(request):
    return render(request , 'single-blog.html')

def product_page(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    product_detail = get_object_or_404(ProductDetail, product=product)
    related_products = Product.objects.filter(categories__in=product.categories.all()).exclude(id=product.id).distinct()

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
    else:
        is_favorite = False

    context['product'] = product
    context['product_detail'] = product_detail
    context['without_discount'] = f"{round(product.price / (1 - (product.discount / 100))):,}"
    context['discount_price'] = f"{round((product.price / (1 - (product.discount / 100))) - product.price):,}"
    context['is_favorite'] = is_favorite
    context['related_products'] = related_products

    comments = Comment.objects.filter(product=product).prefetch_related('advantages', 'disadvantages')
    context['comments'] = comments
    comment_count = Comment.objects.filter(product=product).count()
    context['comment_count'] = comment_count

    if product.count > 0:
        return render(request, 'single-product.html', context)
    else:
        return render(request, 'single-product-not-available.html', context)

def comparison_page(request):
    return render(request , 'product-comparison.html')

def profile_comments(request):
    return render(request , 'profile-comments.html')

@login_required
def add_remove_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()
    
    return redirect(product_page, id=product_id)

def profile_order_details(request):
    return render(request , 'profile-order-details.html')

def profile_favorites(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')

    favorites = Favorite.objects.filter(user=request.user)
    context['favorites'] = favorites
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    user_profile = UserProfile.objects.get(user = request.user)
    context['profile'] = user_profile

    return render(request, 'profile-favorites.html', context)

def product_search(request):
    query = request.GET.get('q') 
    products = Product.objects.all() 

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(brand__name__icontains=query) | 
            Q(categories__name__icontains=query)
        ).distinct()

    return render(request, 'search.html', {'products': products})

def remove_favorite(request, product_id):
    favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
    favorite.delete()
    return redirect(profile_favorites)
