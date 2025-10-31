from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

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
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not matched ')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already taken")
            return redirect('register')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request, 'Account created successfully! Login now.')
        return redirect('login')
    return render(request, 'base/register.html')

@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')