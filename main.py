# The termianl application will be run from here

import os

def clear_screen(): # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

# Display locations menu
def displayMenu_locations(locations):
    print("\nSelect your location:")
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location}")

# Display main menu
def displayMenu_main():
    print("\nSelect an option:")
    print("1. View locations")
    print("2. View last 12hr earthquakes")
    print("3. Report an earthquake")
    print("4. Settings")

# Settings
def displayMenu_settings():
    print("\nSelect an option:")
    print("1. Change location")
    print("2. Change notification settings")

def main():
    # NZ regions - this data is a placeholder for now and will later be replaced with data from the database
    locations = ["Northland", "Waikato", "Bay of Plenty", "Hawk's Bay", "Taranaki", "Manawatu-Wanganui", "Wellington", "West Coast", "Canterbury", "Otago", "Southland"]

    # Initial location selection
    while True:
        displayMenu_locations(locations)

        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))

            clear_screen()

            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(locations):
                selected_location = locations[choice - 1]
                print(f"You have selected: {selected_location}")
                break
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

    # Main menu
    while True:
        displayMenu_main()

        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))

            clear_screen()

            if choice == 0:
                print("Exiting...")
                break
            elif choice == 1:
                print("View locations")
            elif choice == 2:
                print("View last 12hr earthquakes")
            elif choice == 3:
                print("Report an earthquake")
            elif choice == 4:
                print("Settings")

                # Display Settings
                while True:
                    displayMenu_settings()

                    try:
                        choice = int(input("\nEnter your choice (or 0 to go back): "))

                        clear_screen()

                        if choice == 0:
                            print("Exiting...")
                            break
                        elif choice == 1:
                            print("Change location")
                        elif choice == 2:
                            print("Change notification settings")
                        else:
                            print("Invalid choice, please try again")
                    except ValueError:
                        print("Invalid choice, please enter a valid number")
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

if __name__ == "__main__":
    main()