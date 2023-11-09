from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class SeismicIntensity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Earthquake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    seismic = models.ManyToManyField(SeismicIntensity)
    street_name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=2193) # New Zealand Transverse Mercator 2000

    def __str__(self):
        return self.name