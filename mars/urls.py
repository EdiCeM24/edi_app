from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feedBack/', views.feedBack, name='feedBack'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('privacy/', views.private, name='privacy'),
    path('port-folio/', views.portfolio, name='portfolio'),
    path('portfolioDetails/', views.portfolioDetails, name='portfolioDetails'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('terms/', views.terms, name='terms'),
]