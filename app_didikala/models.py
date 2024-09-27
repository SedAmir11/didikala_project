from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

user = get_user_model()

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images' , null=True)
    image = models.ImageField(upload_to='products/prodtctdetail/', null=True, blank=True)

    def __str__(self):
        return f" id {self.product.id} = {self.product.name} - {self.image.url}"
    
class SpecialFeature(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return f"{self.title} {self.detail}"

class DetailDescription(models.Model):
    image = models.ForeignKey(Img, on_delete=models.CASCADE, related_name='detail_descriptions')
    detail = models.TextField()

    def __str__(self):
        return f"{self.image} - {self.detail[:30]}..."

class Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='descriptions' , null= True)
    title = models.CharField(max_length=100)
    description_detail = models.ManyToManyField(DetailDescription, related_name='descriptions')

    def __str__(self):
        return f"{self.title} - id {self.product.id} = {self.product.name}"

class SpecificationDetail(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    autocomplete_fields = ['specification_detail'] 

    def __str__(self):
        return f"{self.name} - {self.detail}"

class Specifications(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications' , null=True)
    title = models.CharField(max_length=100)
    specification_detail = models.ManyToManyField(SpecificationDetail, related_name='specifications')

    def __str__(self):
        return f"{self.title} - id {self.product.id} = {self.product.name}"

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    colors = models.ManyToManyField(Color, related_name='products' , blank = True)
    special_features = models.ManyToManyField(SpecialFeature, related_name='products')
    code_number = models.CharField(max_length=50)
    descriptions = models.ManyToManyField(Description, related_name='products' , blank = True)
    reviews = models.TextField(null = True , blank = True)
    specifications = models.ManyToManyField(Specifications, related_name='products')
    images = models.ManyToManyField(Img, related_name='products')

    def __str__(self):
        return self.title_en
    
    
class Favorite(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"