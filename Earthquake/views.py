from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Earthquake
from .serializer import EarthquakeSerializer
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
#from rest_framework_gis.pagination import GeoJsonPagination

class EarthquakeViewSet(viewsets.ModelViewSet):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
