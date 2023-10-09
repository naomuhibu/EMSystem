from django.db import models

class SeismicIntensity(models.Model):
    place_name = models.CharField(max_length=200)
    intensity = models.IntegerField()

    def __str__(self):
        return f"{self.place_name} - Intensity: {self.intensity}"