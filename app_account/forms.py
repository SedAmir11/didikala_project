from django import forms
from django.contrib.auth import get_user_model , password_validation
from django.contrib.auth.forms import UserCreationForm  
from app_account.models import UserProfile

User = get_user_model()

class signupForm(UserCreationForm):
    # email = forms.EmailField(max_length=200 , help_text='Required')

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2']

class additional_info(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'national_id', 'card_no']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email']