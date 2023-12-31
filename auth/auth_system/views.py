from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required
def HomePage(request):
    return render(request, 'index.html', {})

def Register(request):
    if(request.method == 'POST'):
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(user_name, email, password)
        new_user.save()
        return redirect('login-page')

    return render(request, 'register.html', {})

def Login(request):
    if(request.method == 'POST'):
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error: No username or password')

    return render(request, 'login.html', {})    

def logout_view(request):
    logout(request)
    return redirect('login-page')         