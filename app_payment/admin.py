from django.contrib import admin
from app_payment.models import transaction , basket_item , order , order_item , basket


@admin.register(transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(basket_item)
class basket_itemAdmin(admin.ModelAdmin):
    pass

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    pass

@admin.register(order_item)
class order_itemAdmin(admin.ModelAdmin):
    pass

@admin.register(basket)
class basketAdmin(admin.ModelAdmin):
    pass
