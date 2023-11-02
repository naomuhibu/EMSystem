from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import earthquake


class EarthquakeAdmin(LeafletGeoAdmin):
    list_display = ['city', 'district', 'shaking']


admin.site.register(earthquake, EarthquakeAdmin)