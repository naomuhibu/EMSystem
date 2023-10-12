# IMPORTS
import os
import random
import threading
import time

# GLOBAL VARIABLES
locations = ""
selected_location = ""
notifications = True
earthquake_data = {}

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

def update_earthquake_data():
    global earthquake_data
    global notifications
    global selected_location
    while True:
        for location in locations:
            earthquake_data[location] = random.choice([True, False])

        # if notifications enabled and selected location true then print warning
            if notifications and selected_location in earthquake_data and earthquake_data[selected_location]:
                print(f"\nWARNING: Earthquake detected in {selected_location}")
        time.sleep(30)

def view_earthquakes():
    print("\nLocations with earthquakes in the last 12 hours:")
    for location, has_earthquake in earthquake_data.items():
        if has_earthquake:
            print(f"- {location}")


def report_earthquake():
    global earthquake_data
    global selected_location
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
                # set location to true
                earthquake_data[selected_location] = True
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
    global notifications
    while True:
        if notifications == True:
            print("Notifications are currently enabled, would you like to disable them?")
            choice = input("(Y/N): ")
            clear_screen()
            if choice.lower() == "y":
                notifications = False
                print("Notifications have been disabled")
                break
            elif choice.lower() == "n":
                print("Notifications will remain enabled")
                break
            else:
                print("Invalid choice, please try again")
        else:
            print("Notifications are currently disabled, would you like to enable them?")
            choice = input("(Y/N): ")
            clear_screen()
            if choice.lower() == "y":
                notifications = True
                print("Notifications have been enabled")
                break
            elif choice.lower() == "n":
                print("Notifications will remain disabled")
                break
            else:
                print("Invalid choice, please try again")


def main():
    global locations
    locations = ["Northland", "Waikato", "Bay of Plenty", "Hawk's Bay", "Taranaki", "Manawatu-Wanganui", "Wellington", "West Coast", "Canterbury", "Otago", "Southland"]

    # Start the background thread to update earthquake data
    threading.Thread(target=update_earthquake_data, daemon=True).start()

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
