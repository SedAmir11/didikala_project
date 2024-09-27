from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from app_didikala.models import Brand,division ,Product ,banner ,image , Category, Color, Img, SpecialFeature, DetailDescription, Description, SpecificationDetail, Specifications, ProductDetail, Favorite

class imageInline(GenericStackedInline):
    model = image
    extra = 1
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(division)
class divisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['brand']
    search_fields = ['name']

@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    inlines = [imageInline]

@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class Coloradmin(admin.ModelAdmin):
    pass

@admin.register(Img)
class Imgadmin(admin.ModelAdmin):
    search_fields = ['product__name', 'image']
    extra = 1

@admin.register(SpecialFeature)
class SpecialFeatureadmin(admin.ModelAdmin):
    search_fields = ['title', 'detail']

@admin.register(DetailDescription)
class DetailDescriptionadmin(admin.ModelAdmin):
    search_fields = ['image']

@admin.register(Description)
class Descriptionadmin(admin.ModelAdmin):
    search_fields = ['title', 'product__name']
    autocomplete_fields = ['product']

@admin.register(SpecificationDetail)
class SpecificationDetailadmin(admin.ModelAdmin):
    search_fields = ['name', 'detail'] 

@admin.register(Specifications)
class Specificationsadmin(admin.ModelAdmin):
    search_fields = ['title', 'specification_detail__name']
    autocomplete_fields = ['specification_detail']
    list_display = ['title', 'product'] 

@admin.register(ProductDetail)
class ProductDetailadmin(admin.ModelAdmin):
    autocomplete_fields = ['special_features', 'descriptions', 'specifications', 'images', 'product']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')