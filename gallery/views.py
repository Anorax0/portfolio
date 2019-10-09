from django.shortcuts import render, HttpResponse, redirect
from .models import GalleryItems
from .forms import GalleryForm


def chunks(seq, size):
    return (seq[i::size] for i in range(size))


def index(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        images_all = list(GalleryItems.objects.all().filter(is_published=True))
        images = list(chunks(images_all, 4))

        form = GalleryForm()
        return render(request, 'pages/gallery.html',
                      {'images_col1': images[0], 'images_col2': images[1],
                       'images_col3': images[2], 'images_col4': images[3],
                       'image': None, 'form': form})


def image(request, image_id):
    image = GalleryItems.objects.get(pk=image_id)
    return render(request, 'pages/gallery.html', {'image': image})
