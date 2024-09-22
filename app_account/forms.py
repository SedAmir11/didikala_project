from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm  , PasswordChangeForm
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
        fields = ['profile_picture', 'phone_number', 'national_id', 'card_no' , 'is_Subscription']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email']


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)