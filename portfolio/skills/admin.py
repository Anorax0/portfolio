from django.contrib import admin

from .models import Skills


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'color', 'percentage')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)


admin.site.register(Skills, SkillsAdmin)
