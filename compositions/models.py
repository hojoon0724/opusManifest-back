from django.db import models


# Create your models here.
class Composition(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    instrumentation = models.CharField(max_length=100)
    vocal_range = models.CharField(max_length=100)
    premiere_by = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    recording_url = models.CharField(max_length=100)
    cover_art = models.CharField(max_length=100)
