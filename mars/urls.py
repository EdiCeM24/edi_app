from django.urls import path
from .import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forgot/', views.forgotPassword, name='forgot'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('port-folio/', views.portfolio, name='port-folio'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    
]