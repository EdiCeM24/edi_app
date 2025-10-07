from django.shortcuts import render

from . models import Blog, BlogVid


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'html/blog.html', {
        "blogs": blogs,
    })
