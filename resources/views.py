from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.http import JsonResponse
from rest_framework import generics
from .models import Earthquake
from .serializers import EarthquakeSerializer

class IndexView(TemplateView):
    template_name = 'index.html'

    def earthquakes(self):
        earthquakes = Earthquake.objects.all()
        serializer = EarthquakeSerializer(earthquakes, many=True)
        geojson_data = serializer.data
        return JsonResponse({'earthquakes': geojson_data}, content_type='application/json', safe=False)
    
class EarthquakeAPI(generics.ListAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
