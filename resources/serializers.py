from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Earthquake, SeismicIntensity

class SeismicIntensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SeismicIntensity
        fields = ('mmi', 'scale_level', 'description')

class EarthquakeSerializer(GeoFeatureModelSerializer):
   # seismic = SeismicIntensitySerializer(many=True, read_only=True)

    class Meta:
        model = Earthquake
        geo_field = 'coordinates'
        fields = ('location_name','mmi')
