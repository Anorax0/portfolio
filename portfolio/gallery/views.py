from .models import GalleryItems
from django.views.generic import ListView


class ListImages(ListView):
    model = GalleryItems
    template_name = 'pages/gallery.html'


def add():
    return None
