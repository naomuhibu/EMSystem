import requests
from django.contrib.gis.geos import Point, GEOSGeometry
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import transform
from django.core.management.base import BaseCommand
from resource.models import SeismicIntensity, Earthquake

class Command(BaseCommand):
    help = 'Fetch and save earthquake data'

    def handle(self, *args, **kwargs):
        api_url = "https://api.geonet.org.nz/intensity/strong/processed/2020p666015"
        earthquake_data = fetch_earthquake_data(api_url)

        if earthquake_data is not None:
            self.stdout.write(self.style.SUCCESS('Successfully got earthquake data'))
            save_earthquake_data(earthquake_data)
        else:
            self.stdout.write(self.style.ERROR('Unable to get earthquake data'))

def fetch_earthquake_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        print(f"Response content: {response.content}")  # Print the response content
        return None

def save_earthquake_data(earthquake_data):
    if "features" in earthquake_data:
        for feature in earthquake_data["features"]:
            if "geometry" in feature and "properties" in feature:
                coordinates = feature["geometry"]["coordinates"]
                mmi_value = feature["properties"]["mmi"]
                location_name = feature["properties"]["name"]

                # Convert coordinates from EPSG:2193 to SRID=4326
                transformed_coordinates = transform_coordinates(coordinates)

                # Save or update SeismicIntensity
                intensity, created = SeismicIntensity.objects.get_or_create(
                    mmi=mmi_value,
                    defaults={
                        'scale_level': f'Scale {mmi_value}',
                        'description': f'Description for Scale {mmi_value}',
                    }
                )

                # Save Earthquake
                earthquake, created = Earthquake.objects.get_or_create(
                    location_name=location_name,
                    defaults={
                        'coordinates': Point(transformed_coordinates, srid=4326),
                        'mmi': intensity,
                    }
                )

                print(f"Location: {location_name}, Coordinates: {transformed_coordinates}, MMI: {mmi_value}")

def transform_coordinates(coordinates):
    # Convert coordinates from EPSG:2193 to SRID=4326
    point_2193 = fromstr(f'POINT({coordinates[0]} {coordinates[1]})', srid=2193)
    point_4326 = point_2193.transform(4326)
    return point_4326

