from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.blog, name='blog'),
    path('profile/', views.profile_view, name='profile')
]    