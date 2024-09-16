from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate
from app_account.forms import signupForm
from app_didikala import views as app_views

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
    return render(request , 'profile.html')

def welcome(request):
    return render(request , 'welcome.html')
