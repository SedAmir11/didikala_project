from rest_framework import serializers
from app_didikala.models import Product , banner , image , Category , ProductDetail , Brand
from django.conf import settings

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id' , 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' , 'name' , 'division']

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    def get_categories(self , obj):
        return CategorySerializer(obj.categories.all() , many = True).data
    
    def get_brand(self , obj):
        return BrandSerializer(obj.brand).data

    class Meta:
        model = Product
        fields = ['id' ,'name','categories','price','brand','image','count','discount','star']

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self , obj):
        return settings.DOMAIN + obj.image.url


    class Meta:
        model = image
        fields = ['id' , 'image' , 'url']


class BannerSerializer(serializers.ModelSerializer):
    image_list = serializers.SerializerMethodField()

    def get_image_list(self , obj):
        # Good
        return ImageSerializer(obj.images , many = True).data
    
        #Bad

        # return [
        #     {
        #         'image' : settings.DOMAIN + img.image.url ,
        #         'url' : img.url
        #     }
        #     for img in obj.images]


    class Meta:
        model = banner
        fields = ['id' , 'title' , 'image_list']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['product_id','id','title_fa','title_en','colors','special_features','code_number','descriptions','reviews','specifications','images']