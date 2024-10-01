from django.contrib import admin
from app_account.models import UserProfile , Address



@admin.register(UserProfile)
class profileAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass