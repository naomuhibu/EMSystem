from rest_framework import serializers
from .models import SeismicIntensity

class SeismicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeismicIntensity
        fields = ['id', 'coordinates', 'mmi', 'date_time']