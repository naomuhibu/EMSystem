from rest_framework import serializers,viewsets
from rest_framework_gis.serializers import GeoFeatureModelSerializer
#from django.core.serializers import serialize
from .models import SeismicIntensity
from EMSystem.models import NZregionalcouncil
#import json

class NZregionalcouncilSerializer(GeoFeatureModelSerializer):
    # A class to serialize locations as GeoJSON compatible data
    class Meta:
        model = NZregionalcouncil
        #geo_field = "location"
        fields = '__all__'

class NZRegionalCouncilViewSet(viewsets.ModelViewSet):
    queryset = NZregionalcouncil.objects.all()
    serializer_class = NZregionalcouncilSerializer

'''
class NZregionalcouncil(serialize.Model):
  
    encjson  = serialize('geojson', NZregionalcouncil.objects.filter(REGC2023_V1_00="13"),
            srid=2193, geometry_field='geom', fields=('regc2023_v_00',) )
    result  = json.loads(encjson)
'''
class SeismicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeismicIntensity
        fields = '__all__'
        #fields = ['id', 'coordinates', 'mmi', 'date_time']


