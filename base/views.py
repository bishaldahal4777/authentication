from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Username or password')
            return redirect('login')
    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return render('login')

def register_user(request):
    pass

def dashboard(request):
    pass