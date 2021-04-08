from django.contrib import admin
from .models import ContactForm, Projects, Skills, Quotes
# from .weather import DarkSkyApi


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'viewed', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'viewed', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'is_published')
    list_display_links = ('id', 'title')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'color', 'percentage')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bg_photo')
    list_display_links = ('id', 'title')


admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
