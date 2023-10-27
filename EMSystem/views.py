import requests
from django.http import JsonResponse
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import NZregionalcouncil
from .serializers import NZregionalcouncilSerializer, SeismicSerializer

class NZRegionalCouncilViewSet(viewsets.ModelViewSet):
    queryset = NZregionalcouncil.objects.all()
    serializer_class = NZregionalcouncilSerializer

api_view(['GET', 'POST'])
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

@api_view(['GET'])
def Seismic_Details(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to get data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://api.geonet.org.nz/intensity?type=measured"
    data = Seismic_Details(api_url)

    if data is not None:
        print("Successfully get data")

        # Parsing the JSON data
        if "features" in data:
            for feature in data["features"]:
                if "geometry" in feature and "properties" in feature:
                    coordinates = feature["geometry"]["coordinates"]
                    mmi = feature["properties"]["mmi"]
                    print(f"Coordinates: {coordinates}, MMI: {mmi}")
    else:
        print("Unable to get data")