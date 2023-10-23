from django.contrib.gis.db import models

class SeismicIntensity(models.Model):
    coordinates = models.PointField()  # Field for coordinates
    mmi = models.IntegerField()  # Field for MMI data
    date_time = models.DateTimeField(auto_now_add=True)  # the data created date and time

    def __str__(self):
        return f"Coordinates: {self.coordinates} - MMI: {self.mmi} - Date and Time: {self.date_time}"