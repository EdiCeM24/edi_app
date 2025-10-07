from django.contrib import admin

from . models import Blog, BlogVid


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'image', 'content')}
    
    
class BlogVidAdmin(admin.ModelAdmin):
    pass  
   
    
admin.site.register(Blog, BlogAdmin) 
   
admin.site.register(BlogVid, BlogVidAdmin)
