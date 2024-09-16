from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate
from app_didikala.models import banner , clothes_product , image

def index(request):
    context = {
        'banner_images' : banner.objects.get(title='home-main').images,
        'clothes_product' : clothes_product.objects.all()
    }
    return render(request , 'index.html' , context)

def notfoundpage(request):
    return render(request , '404.html')

def blog(request):
    return render(request , 'blog.html')

def cart(request):
    return render(request , 'cart.html')

def cart_empty(request):
    return render(request , 'cart-empty.html')

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

def change_password(request):
    return render(request , 'password-change.html')

def verify_phone(request):
    return render(request , 'verify-phone-number.html')

def page_privacy(request):
    return render(request , 'page-privacy.html')

def single_blog(request):
    return render(request , 'single-blog.html')

def product_page(request):
    return render(request , 'single-product.html')

def notavailable_product(request):
    return render(request , 'single-product-not-available.html')

def comment_page(request):
    return render(request , 'product-comment.html')

def comparison_page(request):
    return render(request , 'product-comparison.html')

def additional_info(request):
    return render(request , 'profile-additional-info.html')

def profile_addresses(request):
    return render(request , 'profile-addresses.html')

def profile_comments(request):
    return render(request , 'profile-comments.html')

def profile_favorites(request):
    return render(request , 'profile-favorites.html')

def profile_order_details(request):
    return render(request , 'profile-order-details.html')