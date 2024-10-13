from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from app_didikala.models import Product


user = get_user_model()


class Advantage(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Disadvantage(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Comment(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=255 , null=True)
    description = models.TextField( null=True)
    advantages = models.ManyToManyField(Advantage, related_name='comments')
    disadvantages = models.ManyToManyField(Disadvantage, related_name='comments')
    suggest = models.CharField(max_length=50, choices=[
        ('yes', 'پیشنهاد می‌کنم'),
        ('no', 'پیشنهاد نمی‌کنم'),
        ('no_opinion', 'نظری ندارم'),
    ], null=True)
    creation_date = models.DateTimeField(auto_now_add=True , null=True)
    build_quality = models.IntegerField(null=True, blank=True)
    value_for_price = models.IntegerField(null=True, blank=True)
    innovation = models.IntegerField(null=True, blank=True)
    features_and_capabilities = models.IntegerField(null=True, blank=True)
    ease_of_use = models.IntegerField(null=True, blank=True)
    design_and_appearance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class image(models.Model):
    image = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null=True)
    object_id = models.PositiveIntegerField( null=True)
    content_object = GenericForeignKey("content_type", "object_id")
    
    def __str__(self):
        return self.image.url

