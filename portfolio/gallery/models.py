from django.db import models
from datetime import datetime


class GalleryItems(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=300)
    title = models.TextField(default='Image')
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return self.title
