import requests

def fetch_data_from_api(api_url):
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
    data = fetch_data_from_api(api_url)

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
