from django.urls import path
from . import views

urlpatterns = [
    path('api-products/', views.apiproduct_list, name='api-product-list'),
    path('api-products/create/', views.apiproduct_create, name='product-create'),
    path('api-products/delete/', views.apiproduct_delete, name='product-delete'),
    path('api-products/update/', views.apiproduct_update, name='product-update'),
    path('api-product-details/', views.apiproductdetail_list, name='product-detail-list'),
    path('banner/', views.banner_list_api, name='api-banner'),
    
]