from django.db import models


# Create your models here.
class Composition(models.Model):
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, blank=True)
    year = models.CharField(max_length=4, blank=True)
    instrumentation = models.CharField(max_length=254, blank=True)
    category = models.CharField(max_length=100, blank=True)
    notes = models.TextField(default="", blank=True)
