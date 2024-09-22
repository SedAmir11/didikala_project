from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(user , on_delete=models.CASCADE , null= True)
    phone_number = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255)
    card_no = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="usersimage" ,  null = True)
    is_Subscription = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} profile"


class address(models.Model):
    user =  models.OneToOneField(user , on_delete=models.CASCADE , null= True)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
