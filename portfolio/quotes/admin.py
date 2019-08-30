from django.contrib import admin

from .models import Quotes


class QuotesAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Quotes, QuotesAdmin)