from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


user = get_user_model()

class point(models.Model):
    """
    نقاط قوت و ضعف
    """
    type = models.BooleanField()
    description = models.TextField()


class is_Useful(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    is_useful = models.BooleanField()


class comment(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    description = models.TextField()
    suggest = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    point = models.ForeignKey(point , on_delete=models.CASCADE)
    is_useful = models.ForeignKey(is_Useful , on_delete=models.CASCADE)


class image(models.Model):
    image = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null=True)
    object_id = models.PositiveIntegerField( null=True)
    content_object = GenericForeignKey("content_type", "object_id")
    
    def __str__(self):
        return self.image.url

