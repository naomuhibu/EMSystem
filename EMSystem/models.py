from django.db import models

class Seismic_intensity_data(models.Model):
    place_name = models.CharField(max_length=200)
    intensity = models.IntegerField()
    