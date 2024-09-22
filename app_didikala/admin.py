from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from app_didikala.models import Brand,division ,Product ,banner ,image , Category, Color, Img, SpecialFeature, DetailDescription, Description, SpecificationDetail, Specifications, ProductDetail
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
    pass

@admin.register(SpecialFeature)
class SpecialFeatureadmin(admin.ModelAdmin):
    pass

@admin.register(DetailDescription)
class DetailDescriptionadmin(admin.ModelAdmin):
    pass

@admin.register(Description)
class Descriptionadmin(admin.ModelAdmin):
    pass

@admin.register(SpecificationDetail)
class SpecificationDetailadmin(admin.ModelAdmin):
    pass

@admin.register(Specifications)
class Specificationsadmin(admin.ModelAdmin):
    pass

@admin.register(ProductDetail)
class ProductDetailadmin(admin.ModelAdmin):
    autocomplete_fields = ['product']
    list_display = ['product', 'title_en', 'code_number']  # فیلدهایی که در لیست نمایش داده شوند
    search_fields = ['product__name', 'title_en']  # قابلیت جستجو بر اساس نام محصول و عنوان انگلیسی
    list_filter = ['product__categories']  # فیلتر بر اساس کتگوری محصول
