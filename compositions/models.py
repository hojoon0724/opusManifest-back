from django.db import models


# Create your models here.
class Composition(models.Model):
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, blank=True)
    year = models.IntegerField
    instrumentation = models.CharField(max_length=254, blank=True)
    premiere_date = models.DateField
    publisher = models.CharField(max_length=100, blank=True)
