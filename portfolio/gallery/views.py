from django.shortcuts import render
from django.views.generic import ListView
from .models import GalleryItems


class ListImages(ListView):
    model = GalleryItems
    template_name = 'pages/gallery.html'


def add():
    return None
