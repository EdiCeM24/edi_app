from django.contrib import admin
from . models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'image', 'content')}
    
    
class BlogVidAdmin(admin.ModelAdmin):
    pass  
   
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'profile', 'website', 'github', 'linkedin')
   



admin.site.register(Blog, BlogAdmin) 
   
admin.site.register(BlogVid, BlogVidAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
