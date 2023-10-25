import os
from request import extractData, getNearestLocation

def main():
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

    print("\n--- Earthquake Early Warning System ---\n")
    extractedData = []
    extractedData = extractData()

    # Display extracted data
    for each in extractedData:
        a = [each[0], each[1]]
        left = f'Coords: [{each[1]}, {each[0]}] '
        right = f'Nearest Location: {getNearestLocation(a, location_coordinates)}'
        print(f'{left:<40}{right:>40}')

if __name__ == "__main__":
    main()