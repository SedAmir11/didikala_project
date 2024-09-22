"""
URL configuration for didikala_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from app_didikala import views

urlpatterns = [
    path('' , views.index),
    path('NotFound/' , views.notfoundpage),
    path('blog/' , views.blog),
    path('cart/' , views.cart),
    path('cart-empty/' , views.cart_empty),
    path('cart-empty-next-list/' , views.cart_empty_next_list),
    path('homepage/' , views.index2),
    path('page-faq/' , views.page_faq),
    path('page-faq-category/' , views.page_faq_category),
    path('page-faq-question/' , views.page_faq_question),
    path('verify-phone-number/' , views.verify_phone),
    path('page-privacy/' , views.page_privacy),
    path('single-blog/' , views.single_blog),
    path('single-product/<int:id>/details/' , views.product_page , name='product_page'),
    path('single-product-not-available/' , views.notavailable_product), 
    path('product-comment/' , views.comment_page), 
    path('product-comparison/' , views.comparison_page), 
    path('profile-additional-info/' , views.additional_info), 
    path('profile-addresses/' , views.profile_addresses), 
    path('profile-comments/' , views.profile_comments), 
    path('profile-favorites/' , views.profile_favorites), 
    path('profile-order-details/' , views.profile_order_details), 
]
