from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

class Brand(models.Model):
    name = models.CharField(max_length=255 , null=True)

    def __str__(self):
        return self.name

class division(models.Model):
    name = models.CharField(max_length=255 , null=True)

    def __str__(self):
        return f"id = {self.id} {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255 , null=True)
    division = models.ForeignKey(division, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return f"id = {self.id} {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255 , null=True)
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=0 , null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE , null=True)
    image = models.ImageField(upload_to='products/' , null=True)
    count = models.IntegerField(null=True)
    discount = models.DecimalField(max_digits=10 , decimal_places = 0 , null=True)
    star = models.IntegerField(null=True)

    def formatted_price(self):
        if self.price is not None:
            return "{:,.0f}".format(self.price)
        return "0"

    def __str__(self):
        return f"id = {self.id} {self.name}"


class banner(models.Model):
    title = models.CharField(max_length=255 , null=True)

    @property
    def images(self):
        return image.objects.filter(object_id = self.id ,
                                    content_type = ContentType.objects.get_for_model(self.__class__).id)


class image(models.Model):
    url = models.CharField(max_length=150 , null=True)
    image = models.ImageField(upload_to='store/images/' , null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null=True ,related_name='app_didikala_images')
    object_id = models.PositiveIntegerField( null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.url

class Color(models.Model):
    color_code = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20 , null= True)

    def __str__(self):
        return self.color_name

class Img(models.Model):
    image = models.ImageField(upload_to='products/prodtctdetail/', null=True, blank=True)  # امکان آپلود تصویر
    def __str__(self):
        return str(self.image.url)
    
class SpecialFeature(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.title

class DetailDescription(models.Model):
    image = models.ForeignKey(Img, on_delete=models.CASCADE, related_name='detail_descriptions')
    detail = models.TextField()

    def __str__(self):
        return f"{self.image} - {self.detail[:30]}..." # نمایش مختصر از detail

class Description(models.Model):
    title = models.CharField(max_length=100)
    description_detail = models.ManyToManyField(DetailDescription, related_name='descriptions')

    def __str__(self):
        return self.title

class SpecificationDetail(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return self.name

class Specifications(models.Model):
    title = models.CharField(max_length=100)
    specification_detail = models.ManyToManyField(SpecificationDetail, related_name='specifications')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.title

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    colors = models.ManyToManyField(Color, related_name='products' , null = True , blank = True)
    special_features = models.ManyToManyField(SpecialFeature, related_name='products')
    code_number = models.CharField(max_length=50)
    descriptions = models.ManyToManyField(Description, related_name='products' , null = True , blank = True)
    reviews = models.TextField(null = True , blank = True)
    specifications = models.ManyToManyField(Specifications, related_name='products')
    images = models.ManyToManyField(Img, related_name='products')

    def __str__(self):
        return self.title_en
    
    
