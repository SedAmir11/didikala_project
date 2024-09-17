from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate
from app_account.forms import signupForm , additional_info , UserUpdateForm
from app_didikala import views as app_views
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    context = {}
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request , user)
            context['form'] = form
            return redirect(welcome)
    else:
        context['form'] = signupForm
    return render(request , 'register.html' , context)

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect(app_views.index)
    return render(request , 'login.html')

def profile(request):
    context = {}
    try:
        additional_info(request.user.userprofile)
    except ObjectDoesNotExist:
        UserProfile.objects.create(user = request.user)

    user_profile = UserProfile.objects.get(user = request.user)
    print(user_profile.profile_picture.url)
    context['profile'] = user_profile
    return render(request , 'profile.html' , context)

def welcome(request):
    return render(request , 'welcome.html')

def additional_info_profile(request):
    context = {}
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    national_id = request.POST.get('national_id')
    card_no = request.POST.get('card_no')

    try:
        additional_info(request.user.userprofile)
    except ObjectDoesNotExist:
        UserProfile.objects.create(user = request.user)

    user_profile = UserProfile.objects.get(user = request.user)
    context['profile'] = user_profile

    if request.method == 'POST':
        form = UserUpdateForm(request.POST , instance=request.user)
        if first_name != None and last_name != None and email != None:
            form.save()
            form = additional_info(data = request.POST , instance=request.user.userprofile , files= request.FILES)
            if phone_number != None and national_id != None and card_no != None :
                form.save()
                return redirect(app_views.index)
        
    return render(request , 'profile-additional-info.html' , context)

def personal_info_profile(request):
    context = {}
    try:
        additional_info(request.user.userprofile)
    except ObjectDoesNotExist:
        UserProfile.objects.create(user = request.user)

    user_profile = UserProfile.objects.get(user = request.user)
    print(user_profile.profile_picture.url)
    context['profile'] = user_profile
    return render(request , "profile-personal-info.html" , context)