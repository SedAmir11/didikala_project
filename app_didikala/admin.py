from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from app_didikala.models import brand,digital_product ,color ,banner ,image , clothes_product , category

class imageInline(GenericStackedInline):
    model = image
    extra = 1

@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
    pass

@admin.register(digital_product)
class digital_productAdmin(admin.ModelAdmin):
    inlines = [imageInline]

@admin.register(clothes_product)
class clothes_productAdmin(admin.ModelAdmin):
    inlines = [imageInline]

@admin.register(color)
class colorAdmin(admin.ModelAdmin):
    pass

@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    inlines = [imageInline]

@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    pass

