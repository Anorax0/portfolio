from django.shortcuts import render
from .models import GalleryItems


def chunks(seq, size):
    return (seq[i::size] for i in range(size))


def index(request):
    images_all = list(GalleryItems.objects.all().filter(is_published=True))
    images = list(chunks(images_all, 4))
    return render(request, 'pages/gallery.html',
                  {'images_col1': images[0], 'images_col2': images[1],
                   'images_col3': images[2], 'images_col4': images[3]})


def add():
    return None
