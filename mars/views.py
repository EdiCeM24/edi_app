from django.shortcuts import render, redirect
from django.contrib.auth.models import auth



def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def signup(request):
    return render(request, 'home/signup.html')


def login(request):
    return render(request, 'home/login.html')


def portfolio(request):
    return render(request, 'home/portfolio.html')


def resume(request):
    return render(request, 'home/resume.html')


def services(request):
    return render(request, 'home/services.html')


def forgotPassword(request):
    return render(request, 'home/forgot.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
