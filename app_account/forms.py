from django import forms
from django.contrib.auth import get_user_model , password_validation
from django.contrib.auth.forms import UserCreationForm  

User = get_user_model()

class signupForm(UserCreationForm):
    # email = forms.EmailField(max_length=200 , help_text='Required')

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2']