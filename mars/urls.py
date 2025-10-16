from django.urls import path
from .import views


urlpatterns = [
    path(
        '', 
        views.home, 
        name='home'
    ),

    path(
        'about/', 
        views.about, 
        name='about'
    ),

    path(
        'blogs/', 
        views.blog, 
        name='blog'
    ),
    
    path(
        'contact/', 
        views.contact, 
        name='contact'
    ),
    
    path(
        'contact_success/', 
        views.contact_success, 
        name='contact_success'
    ),
    
    path(
        'dashboard/', 
        views.dashboard, 
        name='dashboard'
    ),
    
    path(
        'feedBack/', 
        views.feedBack, 
        name='feedBack'
    ),
    
    path(
        'login/', 
        views.loginView, 
        name='login'
    ),
    
    path(
        'logout/', 
        views.logout, 
        name='logout'
    ),
    
    path(
        'privacy/', 
        views.private, 
        name='privacy'
    ),
    
    path(
        'port-folio/', 
        views.portfolio, 
        name='portfolio'
    ),
    
    path(
        'portfolioDetails/', 
        views.portfolioDetails, 
        name='portfolioDetails'
    ),
    
    path(
        'forgot-password/', 
        views.ForgotPassword, 
        name='forgot-password'
    ),
    
    path(
        'password-reset-sent/<str:reset_id>/', 
        views.PasswordResetSent, 
        name='password-reset-sent'
    ),
    
    path(
        'reset-password/<str:reset_id>/', 
        views.ResetPassword, 
        name='reset-password'
    ),
    
    path(
        'resume/', 
        views.resume, 
        name='resume'
    ),

    path(
        'services/', 
        views.services, 
        name='services'
    ),
    
    path(
        'register/', 
        views.registerView, 
        name='register'
    ),

    path(
        'terms/', 
        views.terms, 
        name='terms'
    ),
]