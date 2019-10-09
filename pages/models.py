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


class Skills(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    percentage = models.PositiveSmallIntegerField()
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.URLField()
    is_published = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Quotes(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    source = models.CharField(max_length=5)
    bg_photo = models.ImageField(upload_to='images/%Y/%m/%d/')

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.title
