from django.contrib import admin
from.models import Skill



class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'numInPercentage')



admin.site.register(Skill, SkillAdmin)

