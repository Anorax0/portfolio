from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.URLField()
    is_published = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
