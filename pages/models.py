from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from random import choice
import logging

log = logging.getLogger(__name__)


class About(models.Model):
    content = RichTextField()

    class Meta:
        verbose_name = "About Form"

    def __str__(self):
        return "About entry"


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)

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

    @classmethod
    def get_all(cls):
        try:
            return cls.objects.all()
        except Exception as e:
            log.error("Cannot retrieve Skills from database due to error: ", e)


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

    @classmethod
    def get_all(cls):
        try:
            return cls.objects.filter(is_published=True)
        except Exception as e:
            log.error("Cannot retrieve Projects from database due to error: ", e)


class Quotes(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    source = models.CharField(max_length=5)
    bg_photo = models.ImageField(upload_to="images/%Y/%m/%d/")

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.title

    @classmethod
    def get_random_quote(cls):
        try:
            all_quotes = cls.objects.values_list("id", flat=True)
            random_quote = choice(all_quotes)
            quote = cls.objects.get(id=random_quote)
            return quote
        except Exception as e:
            log.error("Cannot retrieve Quotes from database due to error: ", e)
