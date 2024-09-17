from django.contrib import admin
from app_account.models import UserProfile , address



@admin.register(UserProfile)
class profileAdmin(admin.ModelAdmin):
    pass

@admin.register(address)
class addressAdmin(admin.ModelAdmin):
    pass