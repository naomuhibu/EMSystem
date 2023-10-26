from django.contrib import admin
from django.contrib.gis import admin
from .models import SeismicIntensity, NZregionalcouncil

class SeismicIntensityAdmin(admin.ModelAdmin):
    list_display = ('id', 'coordinates', 'mmi', 'date_time', 'geom')  # Customize the displayed fields
    list_filter = ('mmi',)  # Add filters
    search_fields = ('coordinates',)  # Add search fields
'''
class NZregionalcouncilAdmin(gis_admin.OSMGeoAdmin):  # Use gis_admin.OSMGeoAdmin for spatial data
    list_display = ('id', 'regc2023_v', 'regc2023_1', 'regc2023_2', 'land_area_field', 'area_sq_km', 'shape_leng', 'geom')
    list_filter = ('regc2023_1', 'regc2023_2')  # Add filters
    search_fields = ('regc2023_v', 'regc2023_1', 'regc2023_2')  # Add search fields
'''
# Register the models with the customized admin classes
admin.site.register(SeismicIntensity, SeismicIntensityAdmin)
admin.site.register(NZregionalcouncil, admin.OSMGeoAdmin)