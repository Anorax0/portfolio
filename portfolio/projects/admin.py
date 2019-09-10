from django.contrib import admin

from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'is_published')
    list_display_links = ('id', 'title')


admin.site.register(Projects, ProjectsAdmin)
