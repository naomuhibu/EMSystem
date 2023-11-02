from rest_framework import viewsets

from .models import Earthquake
from .serializers import EarthquakeSerailizer

class EarthquakeViewSet(viewsets.ModelViewSet):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerailizer