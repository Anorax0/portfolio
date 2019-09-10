from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    percentage = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
