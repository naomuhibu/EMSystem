from django.db import models
from django.contrib.gis.db import models as gis_models

class SeismicIntensity(models.Model):
    mmi = models.IntegerField(unique=True)
    scale_level = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return str(self.mmi)

class Earthquake(models.Model):
    location_name = models.CharField(max_length=50, unique=True)
    coordinates = gis_models.PointField(srid=4326)  
    mmi = models.ForeignKey(SeismicIntensity, on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name
