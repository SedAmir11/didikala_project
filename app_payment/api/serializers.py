from rest_framework import serializers
from app_payment.models import Basket , BasketItem , Product 
from app_didikala.models import Category , Brand
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
        fields = ['name','categories','price','brand','image','count','discount','star']


class BasketItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self , obj):
        return ProductSerializer(obj.product).data

    class Meta:
        model = BasketItem
        fields = ['id' , 'count' , 'product']


class BasketSerializer(serializers.ModelSerializer):
    basket_item = serializers.SerializerMethodField()

    def get_basket_item(self , obj):
        basket_items = obj.items.all() 
        return BasketItemSerializer(basket_items , many = True).data

    class Meta:
        model = Basket
        fields = '__all__'
