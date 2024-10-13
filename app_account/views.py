from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login as auth_login , authenticate , update_session_auth_hash
from app_account.forms import signupForm , additional_info , UserUpdateForm , ChangePasswordForm , AddressForm
from app_didikala import views as app_views
from .models import UserProfile , Address
from django.contrib.auth.decorators import login_required


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

@login_required
def profile(request):
    context = {}
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    context['profile'] = user_profile
    return render(request , 'profile.html' , context)

def welcome(request):
    return render(request , 'welcome.html')

@login_required
def additional_info_profile(request):
    context = {}
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    national_id = request.POST.get('national_id')
    card_no = request.POST.get('card_no')
    
    post = request.POST.copy()
    if request.POST.get('is_Subscription') is not None:
        post['is_Subscription'] = True
        request.POST = post
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
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

@login_required
def personal_info_profile(request):
    context = {}
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    user_profile = UserProfile.objects.get(user = request.user)
    context['profile'] = user_profile
    return render(request , "profile-personal-info.html" , context)

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user , request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request , user)
            return redirect(profile)
    else:
        form = ChangePasswordForm(request.user)
    return render(request , 'password-change.html' , {'form' : form})

@login_required
def profile_addresses(request):
    context = {}
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    context['profile'] = user_profile
    user_addresses = Address.objects.filter(user=request.user)
    context['addresses'] = user_addresses
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
        else:
            form = AddressForm()
    else:
        form = AddressForm()  
    context['form'] = form

    return render(request , 'profile-addresses.html' , context)

@login_required
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    address.delete()
    return redirect('profile_addresses')