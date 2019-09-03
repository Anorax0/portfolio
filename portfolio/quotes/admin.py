from django.contrib import admin

from .models import Quotes


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bg_photo')
    list_display_links = ('id', 'title')


admin.site.register(Quotes, QuotesAdmin)
