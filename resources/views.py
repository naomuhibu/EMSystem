from django.shortcuts import render
from .models import Earthquake
from .serializers import EarthquakeSerializer
from rest_framework import generics
# Create your views here.

class EarthquakeAPI(generics.ListAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer