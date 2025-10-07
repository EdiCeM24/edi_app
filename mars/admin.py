from django.contrib import admin
from .models import Contact, AboutDelivery, Skill, Feed_back, PortfolioDetail, PortVideo, About, AboutSwipe, Portfolio, PortfolioVideo, Services, Term, Privacy_policy



class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'subject', 'company_name', 'website', 'message')
    
    
class AboutDeliveryAdmin(admin.ModelAdmin):
    list_display = ('text', )
    
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'numInPercentage')
    
    
class Feed_backAdmin(admin.ModelAdmin):
    list_display = ('name', 'msg')    
    
    
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'created_at')
    
    
class AboutSwipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'title', 'text', 'created_at')
    
class PortfolioDetailAdmin(admin.ModelAdmin):
    list_display = ('continue_text', 'head_word', 'text', 'display_image', 'author', 'created_at')
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'text', 'readMore', 'created_at')
    
    
class PortVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'continue_from_prev', 'video', 'text', 'created_at')
    
    
class PortfolioVideoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'text', 'readMore', 'created_at')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text', 'created_at')
    
    
class TermAdmin(admin.ModelAdmin):
    list_display = ('caption', 'message', 'author', 'created_time')
    

class Privacy_policyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text_msg', 'author', 'created_at')
    



admin.site.register(Contact, ContactAdmin)

admin.site.register(AboutDelivery, AboutDeliveryAdmin)

admin.site.register(Skill, SkillAdmin)

admin.site.register(About, AboutAdmin)

admin.site.register(AboutSwipe, AboutSwipeAdmin)

admin.site.register(Feed_back, Feed_backAdmin)

admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(PortVideo, PortVideoAdmin)

admin.site.register(PortfolioVideo, PortfolioVideoAdmin)

admin.site.register(PortfolioDetail, PortfolioDetailAdmin)

admin.site.register(Services, ServicesAdmin)

admin.site.register(Term, TermAdmin)

admin.site.register(Privacy_policy, Privacy_policyAdmin)
