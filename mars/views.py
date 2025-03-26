from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import Skill



def home(request):
    return render(request, 'home/index.html')


def about(request):
    labels = []
    data = []
    product = Skill.objects.order_by('numInPercentage')[:9]
    for skills in product:
        labels.append(skills.name)
        data.append(skills.numInPercentage)
    return render(request, 'home/about.html', {
        'product': product,
        'labels': labels,
        'data': data
    })


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
