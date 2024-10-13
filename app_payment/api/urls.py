from django.urls import path
from . import views

urlpatterns = [
    path('api-basket/', views.apibasket_list, name='api-product-list'),
    path('api-basket/delete/', views.apibasket_delete, name='api-product-delete'), 
    path('api-basket/create/', views.apibasket_create, name='api-product-create'), 
    path('api-basket/update/', views.apibasket_update, name='api-product-update'), 
]