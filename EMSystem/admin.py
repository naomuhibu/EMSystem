from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import SeismicIntensity, NZregionalcouncil

class SeismicIntensityAdmin(gis_admin.ModelAdmin):
    list_display = ('id', 'coordinates', 'mmi', 'date_time', 'geom')
    list_filter = ('mmi',)
    search_fields = ('coordinates',)

class NZregionalcouncilAdmin(gis_admin.OSMGeoAdmin):
    list_display = ('id', 'regc2023_v', 'regc2023_1', 'regc2023_2', 'land_area_field', 'area_sq_km', 'shape_leng', 'geom')
    list_filter = ('regc2023_1', 'regc2023_2')
    search_fields = ('regc2023_v', 'regc2023_1', 'regc2023_2')

admin.site.register(SeismicIntensity, SeismicIntensityAdmin)
admin.site.register(NZregionalcouncil, NZregionalcouncilAdmin)
