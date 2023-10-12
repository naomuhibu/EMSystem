from django.http import JsonResponse
from .models import SeismicIntensity
from .serializers import SeismicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view('GET','POST')
def Seismic_list(request):

    if request.method == 'GET':
        EMSystem = SeismicIntensity.objects.all()
        serializer = SeismicSerializer(EMSystem, many=True)
        data = serializer.data
        return JsonResponse({"EMSystem": data})
    if request.method == 'POST':
        serializer = SeismicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        
##@api_view('GET', 'PUT' , 'DELATE')
##def Seismic_Detail(request):

