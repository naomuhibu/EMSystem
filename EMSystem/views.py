from django.http import JsonResponse
from .models import SeismicIntensity
from .serializers import SeismicSerializer

def Seismic_list(request):
    EMSystem = SeismicIntensity.objects.all()
    serializer = SeismicSerializer(EMSystem, many=True)
    data = serializer.data
    return JsonResponse({"EMSystem": data}, safe=False)
