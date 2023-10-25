import os
from request import convertToActiveLocations

def main():

    print("\n--- Earthquake Early Warning System ---\n")
    # extractedData = []
    # extractedData = extractData()

    # Display extracted data
    # for each in extractedData:
    #     a = [each[0], each[1]]
    #     left = f'Coords: [{each[1]}, {each[0]}] '
    #     right = f'Nearest Location: {getNearestLocation(a, location_coordinates)}'
    #     print(f'{left:<40}{right:>40}')

    activeLocations = []
    activeLocations = convertToActiveLocations()

    # print(f'{activeLocations}')
    for locations in activeLocations:
        print(f'{locations}')

if __name__ == "__main__":
    main()