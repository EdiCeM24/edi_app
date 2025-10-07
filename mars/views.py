from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.http import HttpResponse
from .forms import CustomPasswordResetForm
#from apps.userprofile.models import Profile
from django.db import IntegrityError
from django.core.mail import send_mail
from django.urls import reverse_lazy
import uuid
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import loginRequiredMixin
from .models import About, AboutDelivery, AboutSwipe, PortfolioDetail, PortVideo, Contact, Skill, Portfolio, PortfolioVideo, Services, User, Feed_back, Profile, Privacy_policy, Term
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.conf import settings
from .forms import ContactForm
# from .models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout


# @login_required(login_url='/login/')
def home(request):
    return render(request, 'home/index.html')


# @login_required(login_url='/login/')
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
    
    
def blog(request):
    return render(request, 'html/blog.html')    


# @login_required(login_url='/login/')
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
   

def contact_success(request):
    return render(request, 'home/contact_success.html')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'home/dashboard.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname').strip()
        last_name = request.POST.get('lname').strip()
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()
        
        user_data_has_error = False
        
        if User.objects.filter(first_name=first_name).exists():
            user_data_has_error = True
            messages(request, 'First name already exist.')
            return redirect('signup')
        
        if User.objects.filter(last_name=last_name).exists():
            user_data_has_error = True
            messages(request, 'Last name already exist.')
            return redirect('signup')
        
        username = RegexValidator(
            regex=r'^[a-zA-Z0-9@]+$',
            message='Username can only contain alphanumeric characters and at.'
        )
        
         # Check for existing username
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exist! Please try some other username.')
            return redirect('signup')
        
        # Check for existing email
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exist! Please try some other email.')
            return redirect('signup')
         
        
        if len(password1) < 5:
            user_data_has_error = True
            messages.error(request, 'Password1 must be at least 5 characters.')
            return redirect('signup') 
        
        if len(password2) < 5:
            user_data_has_error = True
            messages.error(request, 'Password1 must be at least 5 characters.')
            return redirect('signup') 
            
        # Check password matching    
        if password1 != password2:
            messages.error(request, 'Password do not match.') 
            return redirect('signup')   
        
        try:
            myUser = User.objects.create_user(username, email, password1)
            myUser.first_name = first_name
            myUser.last_name = last_name
            myUser.username = username
            myUser.email = email
            myUser.password1 = password1
            myUser.password2 = password2
            myUser.is_active = False
            myUser.save()
            
            messages.success(request, 'Your account has been created successfully!') 
            return redirect('login')   
                    
        except ValidationError as e:
            messages.error(request, e.messages)
            return redirect('signup')
        
    return render(request, 'home/signup.html')


def verify_email(request, token):
    try:
        user =User.objects.get(email_verification_token=token)
        user.is_active = True
        user.email_verification_token = ''  # I need to fix something here.
        return redirect('login')
    except User.DoesNotExist:
        messages.error(request, 'You have to provide a valid email address.')
        return render(request, 'registration/invalid_token.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if not remember_me:
                request.session.set_expiry(0) # session expires when browser closes.
            else:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)  #session expires after a certain time.    
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials! Please try again.')
            return redirect('login')
        
    return render(request, 'home/login.html')


# @login_required(login_url='/login/')
def portfolio(request):
    ports = Portfolio.objects.all()
    portVid = PortfolioVideo.objects.all()
    return render(request, 'home/portfolio.html', {
        'ports': ports,
        'portVid': portVid,
    })
    

# @login_required(login_url='/login/')
def portfolioDetails(request):
    details = PortfolioDetail.objects.all()
    video = PortVideo.objects.all()
    return render(request, 'home/portfolio-details.html', {
        'details': details,
        'video': video
    })    
    

# @login_required(login_url='/login/')
def resume(request):
    return render(request, 'home/resume.html')


# @login_required(login_url='/login/')
def services(request):
    served = Services.objects.all()
    return render(request, 'home/services.html', {
        'served': served,
    })


def password_reset_request(request):
    if request.method == 'POST':
        # password_reset = request.POST['password_reset']
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm() 
           
    return render(request, 'home/password_reset.html', {'form': form})    
    
    
def password_reset_done(request):
    # You can't directly redirect to password_reset_confirm without a valid token
    # Let's assume you have a specific token and uidb64
    # For demonstration purposes only, you should handle this dynamically.
    #uidb64 = 'your_uidb64'
    #token = 'your_token'
    # return redirect(reverse_lazy('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token}))
    return render(request, 'home/password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'home/password_reset_complete.html')

def password_reset_confirm(request):
    return render(request, 'home/password_reset_confirm.html')


# @login_required(login_url='/login/')
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


# @login_required
def profile_view(request):
    if request.method == 'POST':
        profile = Profile(data=request.POST)
        image = request.POST.get('image')
        profile.image = image
        if profile.is_valid():
                messages.success(request, 'Your profile image has been successfully uploaded!')
                profile.save()
                return redirect('home')
    else:
        messages.error(request, 'Profile image is not uploaded!')
        return redirect('profile')
        
    
    return render(request, 'home/profile.html', {
        'profile': image 
        })    # context is not passed again.


# @login_required(login_url='/login/')
def private(request):
    policy = Privacy_policy.objects.all()
    return render(request, 'home/private.html', {'policy': policy})

# @login_required(login_url='/login/')
def terms(request):
    items = Term.objects.all()
    return render(request, 'home/terms.html', {'items': items})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

