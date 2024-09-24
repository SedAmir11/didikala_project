from django.contrib import admin
from app_payment.models import Transaction, BasketItem, Order, OrderItem, Basket

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'status', 'price')
    search_fields = ('ref_code',)
    list_filter = ('status',)

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'count')
    search_fields = ('product__name',)
    list_filter = ('basket',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction')
    search_fields = ('user__username',)
    list_filter = ('transaction__status',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'count')
    search_fields = ('product__name', 'order__user__username')
    list_filter = ('order',)

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
