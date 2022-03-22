from django.contrib import admin
from django import forms
from .models import About, ContactForm, Projects, Skills, Quotes
from ckeditor.widgets import CKEditorWidget


class AboutAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = About
        fields = "__all__"


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm


admin.site.register(About, AboutAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("id", "viewed", "name", "email", "contact_date")
    list_display_links = ("id", "viewed", "name", "email")
    search_fields = ("name", "email")
    list_per_page = 25


admin.site.register(ContactForm, ContactFormAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "is_published")
    list_display_links = ("id", "title")


admin.site.register(Projects, ProjectsAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_published", "color", "percentage")
    list_display_links = ("id", "name")
    list_editable = ("is_published",)


admin.site.register(Skills, SkillsAdmin)


class QuotesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "bg_photo")
    list_display_links = ("id", "title")


admin.site.register(Quotes, QuotesAdmin)
