from django import forms
from .models import GalleryItems


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryItems
        fields = ('title', 'description', 'image')
