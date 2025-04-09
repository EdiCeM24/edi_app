from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import Skill, About, Portfolio, Services
from . models import Contact
from django.http import HttpResponse


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
    msg = Contact.objects.all()
    context = {'msg': msg}
    
    if request.method == "POST":
        
       contacts = Contact()
       
       #contacts = ContactForm(request.POST)
    
       fname = request.POST.get('fname')
       lname = request.POST.get('lname')
       username = request.POST.get('username')
       email = request.POST.get('email')
       phone_number = request.POST.get('phone_number')
       subject = request.POST.get('subject')
       website = request.POST.get('website')
       message = request.POST.get('message')
       company = request.POST.get('company')
       
       contacts.fname = fname
       contacts.lname = lname
       contacts.username = username
       contacts.email = email
       contacts.phone_number = phone_number
       contacts.subject = subject
       contacts.website = website
       contacts.message = message
       contacts.company = company
       
       
       
       # here you can create validation for the contact form.
       
           
           
       contacts.save()
       return HttpResponse('<h2 target="_blank">Thanks for contacted us!</h2>')
       
    return render(request, 'home/contact.html', {}, context=context)
   


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
