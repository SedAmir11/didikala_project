"""
URL configuration for didikala_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from . import views

urlpatterns = [
    path('login/' , views.login), 
    path('login/register/login' , views.login), 
    path('login/register/register' , views.register), 
    path('login/register/' , views.register),
    path('profile/' , views.profile),
    path('welcome/' , views.welcome),
    path('profile-additional-info/' , views.additional_info_profile),
    path('profile-personal-info/' , views.personal_info_profile),
    path("", include("django.contrib.auth.urls")), 
]
