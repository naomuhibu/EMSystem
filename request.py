# IMPORTS
import requests
import re
import ast

# Fetch raw data
def fetchRawEarthquakeData():
    # Fetch raw data from the API
    print("Fetching earthquake data...")
    try:
        response = requests.get("https://api.geonet.org.nz/intensity?type=measured")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to get data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def extractData():
    # Extract the data into a list of coordinates with magnitudes
    data = fetchRawEarthquakeData()

    if data is not None:
        print("Successfully get data")

        # Parsing the JSON data
        extractedData = []
        if "features" in data:
            for feature in data["features"]:
                if "geometry" in feature and "properties" in feature:
                    coordinates = feature["geometry"]["coordinates"]
                    coords = ast.literal_eval(str(coordinates))
                    mmi = feature["properties"]["mmi"]
                    extractedData.append([coords[0], coords[1], mmi])
            return extractedData

def calculateDistance(coords1, coords2):
    # Calculate the distance between two coordinates
    return

def getNearestLocation(coords):
    # Find the nearest location to a given coordinate
    return

def convertToActiveLocations():
    # Convert the data into a list of active locations
    return