from django.contrib.gis.db import models

class SeismicIntensity(models.Model):
    coordinates = models.PointField()  # Field for coordinates
    mmi = models.IntegerField()  # Field for MMI data
    date_time = models.DateTimeField(auto_now_add=True)  # the data created date and time
    geom     = models.PolygonField(srid=2193)

    def __str__(self):
        return f"Coordinates: {self.coordinates} - MMI: {self.mmi} - Date and Time: {self.date_time}"

class NZregionalcouncil(models.Model):
    regc2023_v = models.CharField(max_length=100)
    regc2023_1 = models.CharField(max_length=100)
    regc2023_2 = models.CharField(max_length=100)
    land_area_field = models.FloatField()
    area_sq_km = models.FloatField()
    shape_leng = models.FloatField()
    geom = models.MultiPolygonField(srid=2193)  # use MultiPolygonField

    def __str__(self):
        return self.regc2023_v  # Specify a string representation of the instance

    class Meta:
        verbose_name = "NZ Regional Council"
        verbose_name_plural = "NZ Regional Councils"