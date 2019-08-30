from django.contrib import admin

from .models import Skills


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'percentage')
    list_display_links = ('id', 'name')


admin.site.register(Skills, SkillsAdmin)
