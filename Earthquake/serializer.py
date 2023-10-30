from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Earthquake

class EarthquakeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Earthquake
        geo_field = 'location'
        fields = ['name', 'district', 'region', 'level']  # Specify the fields you want to include
        read_only_fields = ['id', 'created_at', 'updated_at']
