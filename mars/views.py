from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.http import HttpResponse
from django.db import IntegrityError
from django.urls import reverse_lazy
import uuid
from django.conf import settings
from django.template.loader import render_to_string
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home/index.html')


@login_required(login_url='/login/')
def about(request):
    labels = []
    data = []
    product = Skill.objects.order_by('numInPercentage')[:12]
    for skills in product:
        labels.append(skills.name)
        data.append(skills.numInPercentage)
        
    products = About.objects.all()
    aboutSwiper = AboutSwipe.objects.all() 
    product = AboutDelivery.objects.all()
       
    
    return render(request, 'home/about.html', {
        'product': product,
        'labels': labels,
        'data': data,
        'products': products,
        'aboutSwiper': aboutSwiper,
        'product': product
    })
    
    
@login_required(login_url='/login/')    
def blog(request):
    return render(request, 'html/blog.html')    


@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        
        contacts = Contact()
        
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        company_name = request.POST.get('company_name')
        website = request.POST.get('website')
        message = request.POST.get('message')
        
        if User.objects.filter(email=email):
            messages.error(request, '')
        
        try:
            contacts.first_name = first_name
            contacts.last_name = last_name
            contacts.email = email
            contacts.subject = subject
            contacts.phone_number = phone_number
            contacts.company_name = company_name
            contacts.website = website
            contacts.message = message
        
            messages.success(request, 'Your message is submitted successfully. Thanks!')
            contacts.save()   #The error for contact page when submitted is pointed here.
        
            return redirect('home')
        
        except ValidationError as e:
             messages.error(request, e.messages)
             return redirect('contact')  # contacts = ContactForm()
        
    return render(request, 'home/contact.html')
   

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'home/dashboard.html')

       
def registerView(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName').strip()
        last_name = request.POST.get('lastName').strip()
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password1').strip()
        password2 = request.POST.get('password2').strip()
        
        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists.")
            
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists.")
            
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters long.")

        if password != password2:
            user_data_has_error = True
            messages.error(request, "Passwords do not match.")
        
        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            new_user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login') 
        
    return render(request, 'auth/register.html')


#       remember_me = request.POST.get('remember_me')
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        #authenticate user credentials:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
        
    return render(request, 'auth/login.html')


def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Verify if email exists in the database
        try:
            user = User.objects.get(email=email) 
            
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()
            
            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            full_password_reset_url = f"{request.build_absolute_uri(password_reset_url)}"
            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'   # we replace password_reset_url with full_password_reset_url to generate absolute url.
            
            email_message = EmailMessage(
                'Reset your password',
                email_body,
                settings.EMAIL_HOST_USER,      # Email sender
                [email]   # Email receiver
            )  
            
            email_message.fail_silently = True
            email_message.send()
            
            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)
                
            
        except User.DoesNotExist:
            messages.error(request, f"No user with the email '{email}' found")
            return redirect('forgot-password') 
                  
    return render(request, 'auth/forgot_password.html')


def PasswordResetSent(request, reset_id):
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'auth/password_reset_sent.html')
    else:
        # redirect to forgot password page if reset id is not valid
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')


def ResetPassword(request, reset_id):
    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)
       
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            passwords_have_error = False
            
            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')
                
            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 5 characters long')
                
            
            # Check to make sure link has not expired
            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=30)
                
            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired.')
                
                  
            if passwords_have_error:
                return redirect('reset-password', reset_id=password_reset_id.reset_id)    #I replace reset_id with password_reset_id to fix the error.
            passwords_match = password == confirm_password
            password_is_valid = len(password) >= 5
            
            if passwords_match and password_is_valid:
                reset_id.user.set_password(password)
                #user = password_reset_id.user
                #user.set_password(password)
                #user.save()
                reset_id.user.save()
                reset_id.delete()
                messages.success(request, 'Password reset successfully')
                return redirect('login')
            else:
                messages.error(request, 'Password must be at least 5 characters long and match the confirmation')
                return redirect('reset-password', reset_id=reset_id.reset_id)      
    
    
    except PasswordReset.DoesNotExist:
        
         # redirect to forgot password page if reset id is not valid
         messages.error(request, 'Invalid reset id')
         return redirect('forgot-password')


@login_required(login_url='/login/')
def portfolio(request):
    ports = Portfolio.objects.all()
    portVid = PortfolioVideo.objects.all()
    return render(request, 'home/portfolio.html', {
        'ports': ports,
        'portVid': portVid,
    })
    

login_required(login_url='/login/')
def portfolioDetails(request):
    details = PortfolioDetail.objects.all()
    video = PortVideo.objects.all()
    return render(request, 'home/portfolio-details.html', {
        'details': details,
        'video': video
    })    
    

@login_required(login_url='/login/')
def resume(request):
    return render(request, 'home/resume.html')


@login_required(login_url='/login/')
def services(request):
    served = Services.objects.all()
    return render(request, 'home/services.html', {
        'served': served,
    })



@login_required(login_url='/login/')
def feedBack(request):
    if request.method == 'POST':
        feed_back = Feed_back()
        
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        
        feed_back.name = name
        feed_back.msg = msg
        
        messages.success(request, 'Your feedback is submitted successfully. Thanks!')
        feed_back.save()
        
        return redirect('home')
    else:
        feed_back = Feed_back()
    
    return render(request, 'home/feed-back.html')


@login_required(login_url='/login/')
def private(request):
    policy = Privacy_policy.objects.all()
    return render(request, 'home/private.html', {'policy': policy})

@login_required(login_url='/login/')
def terms(request):
    items = Term.objects.all()
    return render(request, 'home/terms.html', {'items': items})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

