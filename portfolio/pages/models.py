from django.db import models


# class Skills(models.Model):
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=100, blank=True)
#     percentage = models.PositiveSmallIntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class Quotes(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.CharField(max_length=1000)
#     source = models.CharField(max_length=5)
#     bg_photo = models.ImageField(upload_to='images/%Y/%m/%d/')
#
#     def __str__(self):
#         return self.title
