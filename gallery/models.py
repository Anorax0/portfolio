from django.db import models
from django.utils import timezone


class GalleryItems(models.Model):
    image = models.ImageField(upload_to="photos")
    description = models.CharField(max_length=300)
    title = models.CharField(max_length=100, default="Image")
    date = models.DateTimeField(default=timezone.now, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return self.title
