import requests
from django.http import JsonResponse
from .models import SeismicIntensity
from .serializers import SeismicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def Seismic_list(request):
    if request.method == 'GET':
        # Fetch data from the GeoNet API
        api_url = "https://api.geonet.org.nz/intensity?type=measured"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if "features" in data:
                seismic_data = []
                for feature in data["features"]:
                    if "geometry" in feature and "properties" in feature:
                        coordinates = feature["geometry"]["coordinates"]
                        mmi = feature["properties"]["mmi"]
                        seismic_data.append({
                            "coordinates": coordinates,
                            "mmi": mmi
                        })
                return JsonResponse({"SeismicIntensity": seismic_data})
            else:
                return JsonResponse({"SeismicIntensity": []})
        else:
            return JsonResponse({"SeismicIntensity": []})
    
    if request.method == 'POST':
        serializer = SeismicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Seismic_Detail(request, id):
    try:
        seismic_data = SeismicIntensity.objects.get(pk=id)
    except SeismicIntensity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeismicSerializer(seismic_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SeismicSerializer(seismic_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        seismic_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def SeismicDataList(request):
    if request.method == 'GET':
        seismic_data = SeismicIntensity.objects.all()
        serializer = SeismicSerializer(seismic_data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SeismicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)