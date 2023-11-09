from django.contrib import admin
from django.contrib.gis import admin
from .models import SeismicIntensity, Earthquake
# Register your models here.

@admin.register(SeismicIntensity)
class IntensityAdmin(admin.ModelAdmin):
    pass

@admin.register(Earthquake)
class EarthquakeAdmin(admin.OSMGeoAdmin):
    pass