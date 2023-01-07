from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

from django.urls import reverse


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # handle login
            if request.POST['email'] and request.POST['password']:
                try:
                    username = User.objects.get(email=request.POST.get('email')).username
                    user = auth.authenticate(username=username, password=request.POST.get('password'))
                    auth.login(request, user)
                    if request.POST['next'] != '':
                        return redirect(request.POST.get('next'))
                    return redirect('/')
                except User.DoesNotExist:
                    return render(request, 'accounts/login.html', {'error': "User Doesn't Exist"})
                except AttributeError:
                    return render(request, 'accounts/login.html', {'error': "Wrong Credentials. Try Again!"})
            else:
                return render(request, 'accounts/login.html', {'error': "Empty Fields"})
        else:
            return render(request, 'accounts/login.html')
    else:
        return redirect('/')


def signup(request):
    if request.method == "POST":
        # handle sign in
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'accounts/signup.html', {'error': "User Already Exists"})
                except User.DoesNotExist:
                    User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                    )
                    messages.success(
                        request, "Signup Successful!")
                    return redirect(login)
            else:
                return render(request, 'accounts/signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'accounts/signup.html', {'error': "Password's Don't Match"})
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))
