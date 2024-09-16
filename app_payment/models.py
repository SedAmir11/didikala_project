from django.db import models
from app_didikala.models import digital_product
from django.contrib.auth import get_user_model

user = get_user_model()

TRANSACTION_CHOICES = (
    (False , 'faile'),
    (True , 'success'),
)

class order(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    transaction = models.OneToOneField('transaction' , on_delete=models.CASCADE)


class order_item(models.Model):
    order = models.ForeignKey(order , on_delete=models.CASCADE)
    product = models.ForeignKey(digital_product , on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class basket(models.Model): 
    user = models.ForeignKey(user , on_delete=models.CASCADE)


class basket_item(models.Model):
    basket = models.ForeignKey(basket , on_delete=models.CASCADE)
    product = models.ForeignKey(digital_product , on_delete=models.CASCADE)
    count = models.IntegerField()


class transaction(models.Model):
    status = models.BooleanField(default=False , choices=TRANSACTION_CHOICES)
    ref_code = models.CharField(max_length=255)
    price = models.IntegerField()


