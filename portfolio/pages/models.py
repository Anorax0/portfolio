from django.db import models
from datetime import datetime


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return self.name
