from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


user = get_user_model()

class brand(models.Model):
    field = models.CharField(max_length=255 , null=True)

    def __str__(self):
        return self.field

class category(models.Model):
    name = models.CharField(max_length=255 , null=True)

    def __str__(self):
        return self.name

class base_product(models.Model):
    name = models.CharField(max_length=255 , null=True)
    price = models.PositiveIntegerField(null=True)
    count = models.PositiveIntegerField(null=True)
    brand = models.ForeignKey(brand , on_delete= models.CASCADE , null=True)

    @property
    def images(self):
        return image.objects.filter(object_id = self.id ,
                                    content_type = ContentType.objects.get_for_model(self.__class__).id)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class digital_product(base_product):
    category = models.ManyToManyField('category')
    

class clothes_product(base_product):
    category = models.ManyToManyField('category')



class color(models.Model):
    product = models.ManyToManyField(digital_product)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color
    


class banner(models.Model):
    title = models.CharField(max_length=255)

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
    
