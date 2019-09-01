from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25


admin.site.register(ContactForm, ContactFormAdmin)