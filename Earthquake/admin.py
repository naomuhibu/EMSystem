from django.contrib import admin
from .models import Earthquake 
from leaflet.admin import LeafletGeoAdmin
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination

class EarthquakeAdmin(LeafletGeoAdmin):
    list_display = ['name', 'district', 'region', 'level']

admin.site.register(Earthquake, EarthquakeAdmin)