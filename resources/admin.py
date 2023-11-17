from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import SeismicIntensity, Earthquake

@admin.register(Earthquake)
class EarthquakeAdmin(gis_admin.OSMGeoAdmin):
   pass

@admin.register(SeismicIntensity)
class IntensityAdmin(admin.ModelAdmin):
    pass
