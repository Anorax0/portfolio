from django.contrib import admin
from .models import GalleryItems


class GalleryItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "date")
    list_display_links = ("id", "title")
    search_fields = ("id", "title", "description", "is_published")
    list_editable = ("is_published",)
    list_per_page = 25


admin.site.register(GalleryItems, GalleryItemsAdmin)
