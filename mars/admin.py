from django.contrib import admin
from .models import Skill, About, Portfolio, Services



class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'numInPercentage')
    
    
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'created_at')
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'text', 'created_at')
    
    
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text', 'created_at')



admin.site.register(Skill, SkillAdmin)

admin.site.register(About, AboutAdmin)

admin.site.register(Portfolio, PortfolioAdmin)


admin.site.register(Services, ServicesAdmin)

