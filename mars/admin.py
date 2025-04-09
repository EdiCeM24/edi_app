from django.contrib import admin
from .models import Contact, Skill, About, Portfolio, SignupForm, Services



class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone_number', 'subject', 'company_name', 'website', 'message')
    
    
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'numInPercentage')
    
    
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'created_at')
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'text', 'created_at')
    
    
class SignupFormAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'username', 'email')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text', 'created_at')



admin.site.register(Contact, ContactAdmin)

admin.site.register(Skill, SkillAdmin)

admin.site.register(About, AboutAdmin)

admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(Services, ServicesAdmin)

admin.site.register(SignupForm, SignupFormAdmin)

