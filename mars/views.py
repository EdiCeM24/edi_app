from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import Skill, About, Portfolio, Services
from . models import Contact
from django.http import HttpResponse
#from apps.userprofile.models import Profile
from django.contrib import messages


def home(request):
    return render(request, 'home/index.html')


def about(request):
    labels = []
    data = []
    product = Skill.objects.order_by('numInPercentage')[:9]
    for skills in product:
        labels.append(skills.name)
        data.append(skills.numInPercentage)
        
    products = About.objects.all() 
       
    
    return render(request, 'home/about.html', {
        'product': product,
        'labels': labels,
        'data': data,
        'products': products
    })


def contact(request):
   
    if request.method == "POST":
        
       contacts = Contact()
       
       #contacts = ContactForm(request.POST)
    
       fname = request.POST.get('fname')
       lname = request.POST.get('lname')
       email = request.POST.get('email')
       phone_number = request.POST.get('phone_number')
       subject = request.POST.get('subject')
       website = request.POST.get('website')
       message = request.POST.get('message')
       company_name = request.POST.get('company_name')
       
       contacts.fname = fname
       contacts.lname = lname
       contacts.email = email
       contacts.phone_number = phone_number
       contacts.subject = subject
       contacts.website = website
       contacts.message = message
       contacts.company_name = company_name
       
       
       
       # here you can create validation for the contact form.
       
           
       messages.success(request, 'Your message has been submitted successfully. Thanks!') 
          
       contacts.save()
       return redirect('home')
    #    return HttpResponse('<h2 target="_blank">Thanks for contacted us!</h2>')
       
    return render(request, 'home/contact.html', {})
   


def signup(request):
    return render(request, 'home/signup.html')


def login(request):
    return render(request, 'home/login.html')


def portfolio(request):
    ports = Portfolio.objects.all()
    return render(request, 'home/portfolio.html', {
        'ports': ports,
    })


def resume(request):
    return render(request, 'home/resume.html')


def services(request):
    served = Services.objects.all()
    return render(request, 'home/services.html', {
        'served': served,
    })


def forgotPassword(request):
    return render(request, 'home/forgot.html')


def feedBack(request):
    return render(request, 'home/feed-back.html')


def private(request):
    return render(request, 'home/private.html')


def terms(request):
    return render(request, 'home/terms.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
