from rest_framework import serializers
from.models import SeismicIntensity

class SeismicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeismicIntensity
        fields = ['id','place_name','intensity']