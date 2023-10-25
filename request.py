# IMPORTS
import requests
import re
import ast
import math

# Approximate central coordinates for each location.
location_coordinates = {
    "Northland": [-35.7251, 174.3237],  # Whangarei
    "Waikato": [-37.7870, 175.2793],  # Hamilton
    "Bay of Plenty": [-37.6878, 176.1651],  # Tauranga
    "Hawk's Bay": [-39.6395, 176.8492],  # Hastings
    "Taranaki": [-39.0556, 174.0756],  # New Plymouth
    "Manawatu-Wanganui": [-40.3523, 175.6082],  # Palmerston North
    "Wellington": [-41.2865, 174.7762],  # Wellington
    "West Coast": [-42.4574, 171.2108],  # Greymouth
    "Canterbury": [-43.5321, 172.6362],  # Christchurch
    "Otago": [-45.8788, 170.5020],  # Dunedin
    "Southland": [-46.4132, 168.3538]  # Invercargill
}


# Fetch raw data
def fetchRawEarthquakeData():
    # Fetch raw data from the API
    # print("Fetching earthquake data...")
    try:
        response = requests.get("https://api.geonet.org.nz/quake?MMI=3")
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
        # print("Successfully got data")

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

# Calculate the distance between two coordinates - Haversine formula
def calculateDistance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert coordinates from degrees to radians
    lon1, lat1 = math.radians(coord1[0]), math.radians(coord1[1])
    lon2, lat2 = math.radians(coord2[0]), math.radians(coord2[1])

    # Differences in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def getNearestLocation(target_coord, location_coordinates):
    min_distance = float('inf')
    closest_loc = None

    for location, location_coordinates in location_coordinates.items():
        distance = calculateDistance(target_coord, location_coordinates)

        if distance < min_distance:
            min_distance = distance
            closest_loc = location

    return closest_loc

def convertToActiveLocations():
    # Convert the data into a list of active locations
    extractedData = []
    extractedData = extractData()

    activeLocations = []

    # Check active locations and set to true
    for each in extractedData:
        # Check if location already set to active
        thisActiveLocation = getNearestLocation([each[0], each[1]], location_coordinates)
        if thisActiveLocation not in activeLocations:
            activeLocations.append(thisActiveLocation)

    return activeLocations