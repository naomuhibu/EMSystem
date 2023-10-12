# The termianl application will be run from here

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu(locations):
    print("\nSelect your location:")
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location}")

def main():
    # NZ regions
    locations = ["Northland", "Waikato", "Bay of Plenty", "Hawk's Bay", "Taranaki", "Manawatu-Wanganui", "Wellington", "West Coast", "Canterbury", "Otago", "Southland"]

    while True:
        display_menu(locations)

        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))

            clear_screen()

            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(locations):
                selected_location = locations[choice - 1]
                print(f"You have selected: {selected_location}")
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

if __name__ == "__main__":
    main()