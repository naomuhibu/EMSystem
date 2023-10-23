from django.contrib import admin
from .models import SeismicIntensity

class SeismicIntensityAdmin(admin.ModelAdmin):
    list_display = ('id', 'coordinates', 'mmi', 'date_time',)  # Customize the displayed fields
    list_filter = ('mmi',)  # Add filters
    search_fields = ('coordinates',)  # Add search fields

# Register the SeismicIntensity model with the customized admin class
admin.site.register(SeismicIntensity, SeismicIntensityAdmin)