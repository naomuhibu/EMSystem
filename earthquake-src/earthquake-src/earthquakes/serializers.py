from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Earthquake


class EarthquakeSerailizer(GeoFeatureModelSerializer):
    class Meta:
        model = Earthquake
        geo_field = 'location'
        fields = ['city', 'district', 'shaking']
        read_only_fields = ['id', 'created_at', 'updated_at']