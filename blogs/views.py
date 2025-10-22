from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
#from apps.userprofile.models import Profile


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'html/blog.html', {
        "blogs": blogs,
    })
    
@login_required
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
