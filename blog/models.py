from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    director = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    cast_member = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
