import os
from request import fetchRawEarthquakeData, extractData, getNearestLocation

def main():
    location_coordinates = {
    "Northland": [174.4860, 35.6163],
    "Waikato": [175.2793, 37.7870],
    "Bay of Plenty": [176.2497, 38.1368],
    "Hawk's Bay": [176.7416, 39.7711],
    "Taranaki": [174.4385, 39.3534],
    "Manawatu-Wanganui": [175.6082, 40.3523],
    "Wellington": [174.7762, 41.2865],
    "West Coast": [171.4787, 42.4068],
    "Canterbury": [171.1637, 43.7545],
    "Otago": [169.8923, 45.1521],
    "Southland": [167.7188, 45.8621]
    }

    print("\n--- Earthquake Early Warning System ---\n")
    extractedData = []
    extractedData = extractData()

    # Display extracted data
    for each in extractedData:
        # print(f'Coords: [{each[0]}, {each[1]}] MMI: {each[2]}')
        a = [each[0], each[1]]
        left = f'Coords: [{each[0]}, {each[1]}] '
        right = f'Nearest Location: {getNearestLocation(a, location_coordinates)}'
        print(f'{left:<40}{right:>40}')
        # print(f'Coords: [{each[0]}, {each[1]}] Nearest Location: {getNearestLocation(a, location_coordinates)}')

if __name__ == "__main__":
    main()