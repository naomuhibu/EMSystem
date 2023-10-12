# IMPORTS
import os

# GLOBAL VARIABLES
selected_location = ""

def clear_screen(): # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

def displayMenu_locations(locations):
    while True:
        print("\nSelect your location:")
        for index, location in enumerate(locations, 1):
            print(f"{index}. {location}")
        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))
            if 0 <= choice <= len(locations):
                return choice
            else:
                clear_screen()
                print("Invalid choice, please try again")
        except ValueError:
            clear_screen()
            print("Invalid choice, please enter a valid number")

def displayMenu_main():
    while True:
        print("\nSelect an option:")
        print("1. View last 12hr earthquakes")
        print("2. Report an earthquake")
        print("3. Settings")
        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))
            if 0 <= choice <= 3:
                return choice
            else:
                clear_screen()
                print("Invalid choice, please try again")
        except ValueError:
            clear_screen()
            print("Invalid choice, please enter a valid number")

def displayMenu_settings():
    while True:
        print("\nSelect an option:")
        print("1. Change location")
        print("2. Change notification settings")
        try:
            choice = int(input("\nEnter your choice (or 0 to go back): "))
            if 0 <= choice <= 2:
                return choice
            else:
                clear_screen()
                print("Invalid choice, please try again")
        except ValueError:
            clear_screen()
            print("Invalid choice, please enter a valid number")

def view_earthquakes():
    # Placeholder function
    print("View last 12hr earthquakes\n- Nothing here yet")

def report_earthquake():
    while True:
        print("\nHow strong does it feel?")
        print("1. Weak")
        print("2. Moderate")
        print("3. Strong")
        print("4. Severe")
        try:
            choice = int(input("\nEnter your choice (or 0 to go back): "))
            clear_screen()
            if 1 <= choice <= 4:
                # Send report
                newReport = selected_location + " " + str(choice)
                print(f"Report Sent:\nLocation: {selected_location}\nStrength: {choice}")
                print
                return
            else:
                clear_screen()
                print("Invalid choice, please try again")
        except ValueError:
            clear_screen()
            print("Invalid choice, please enter a valid number")


def change_location(locations):
    # Reuse the displayMenu_locations function
    choice = displayMenu_locations(locations)
    clear_screen()
    if choice != 0:
        global selected_location
        selected_location = locations[choice - 1]
        print(f"You have changed your location to: {selected_location}")

def change_notifications():
    # Placeholder function
    print("Change notification settings\n- Nothing here yet")

def main():
    locations = ["Northland", "Waikato", "Bay of Plenty", "Hawk's Bay", "Taranaki", "Manawatu-Wanganui", "Wellington", "West Coast", "Canterbury", "Otago", "Southland"]

    choice = displayMenu_locations(locations)
    clear_screen()
    if choice == 0:
        print("Exiting...")
        return
    global selected_location
    selected_location = locations[choice - 1]
    print(f"You have selected: {selected_location}")

    while True:
        choice = displayMenu_main()
        clear_screen()
        if choice == 0:
            print("Exiting...")
            break
        elif choice == 1:
            view_earthquakes()
        elif choice == 2:
            report_earthquake()
        elif choice == 3:
            choice = displayMenu_settings()
            clear_screen()
            if choice == 1:
                change_location(locations)
            elif choice == 2:
                change_notifications()

if __name__ == "__main__":
    main()