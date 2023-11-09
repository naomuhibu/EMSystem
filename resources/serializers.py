from .models import Earthquake, SeismicIntensity
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.fields import GeometryField

class SeismicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeismicIntensity
        fields = ('name',)

class EarthquakeSerializer(GeoFeatureModelSerializer):

    seismic = SeismicSerializer(many=True)

    class Meta:
        model = Earthquake
        geo_field = "location"
        fields = ('name','seismic','street_name')
        