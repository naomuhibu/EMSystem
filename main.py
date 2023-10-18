# IMPORTS
import os
import threading
import time

# GLOBAL VARIABLES
locations = ""
selected_location = ""
notifications = True
earthquake_data = {}

# FUNCTIONS
def clear_screen(): # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

def displayHeader(): # Display the header
    clear_screen()
    print("Earthquake Early Warning System")
    print("================================")
    print(f'Location: {selected_location} | Last Updated: {time.strftime("%H:%M:%S")}')
    if notifications and selected_location in earthquake_data and earthquake_data[selected_location]:
        print(f"\n\033[1m\033[31mWARNING: Earthquake detected in your region.\033[0m")

def displayMenu_locations(locations): # Display the locations menu
    while True:
        print("\nSelect your location:")
        for index, location in enumerate(locations, 1):
            print(f"{index}. {location}")
        try:
            choice = int(input("\nEnter your choice (or 0 to exit): "))
            if 0 <= choice <= len(locations):
                return choice
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

def displayMenu_main(): # Display the main menu
    displayHeader()
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
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

def displayMenu_settings(): # Display the settings menu
    displayHeader()
    while True:
        print("\nSelect an option:")
        print("1. Change location")
        print("2. Change notification settings")
        try:
            choice = int(input("\nEnter your choice (or 0 to go back): "))
            if 0 <= choice <= 2:
                return choice
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")

def update_earthquake_data():   # Update the earthquake data every 30 seconds
    global earthquake_data
    global notifications
    global selected_location
    while True:
        # Fetch the earthquake data
        print("Fetching earthquake data...")
        time.sleep(30)

def view_earthquakes(): # View the current earthquakes
    displayHeader()
    while True:
        print("\nLocations with earthquakes in the last 12 hours:")
        for location, has_earthquake in earthquake_data.items():
            if has_earthquake:
                print(f"- {location}")
        # press any key to continue
        input("\nPress any key to continue...") #FIXME: This is a hacky way to pause the program, find a better way to do this
        break


def report_earthquake():    # Report an earthquake at current location
    global earthquake_data
    global selected_location

    displayHeader()
    while True:
        print("\nHow strong does it feel?")
        print("1. Weak")
        print("2. Moderate")
        print("3. Strong")
        print("4. Severe")
        try:
            choice = int(input("\nEnter your choice (or 0 to go back): "))
            if 1 <= choice <= 4:
                # Send report
                newReport = selected_location + " " + str(choice)
                print(f"Report Sent:\nLocation: {selected_location}\nStrength: {choice}")
                # set location to true
                earthquake_data[selected_location] = True
                return
            elif choice == 0:
                break
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please enter a valid number")


def change_location(locations): # Change the current location
    # Reuse the displayMenu_locations function
    displayHeader()
    choice = displayMenu_locations(locations)
    if choice != 0:
        global selected_location
        selected_location = locations[choice - 1]



def change_notifications(): # Change the notification settings
    global notifications

    displayHeader()
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
            if choice.lower() == "y":
                notifications = True
                print("Notifications have been enabled")
                break
            elif choice.lower() == "n":
                print("Notifications will remain disabled")
                break
            else:
                print("Invalid choice, please try again")

        input("\nPress any key to continue...") #FIXME: This is a hacky way to pause the program, find a better way to do this
        break


def main():
    global locations
    global selected_location
    global earthquake_data

    locations = ["Northland", "Waikato", "Bay of Plenty", "Hawk's Bay", "Taranaki", "Manawatu-Wanganui", "Wellington", "West Coast", "Canterbury", "Otago", "Southland"]

    # Start the background thread to update earthquake data
    threading.Thread(target=update_earthquake_data, daemon=True).start()

    choice = displayMenu_locations(locations)
    if choice == 0:
        print("Exiting...")
        return
    selected_location = locations[choice - 1]
    print(f"You have selected: {selected_location}")

    # if notifications enabled and selected location true then print warning
    if notifications and selected_location in earthquake_data and earthquake_data[selected_location]:
        print(f"\n\033[1m\033[31mWARNING: Earthquake detected in your region.\033[0m")

    while True:
        choice = displayMenu_main()
        if choice == 0:
            clear_screen()
            print("Exiting...")
            break
        elif choice == 1:
            view_earthquakes()
        elif choice == 2:
            report_earthquake()
        elif choice == 3:
            choice = displayMenu_settings()
            if choice == 1:
                change_location(locations)
            elif choice == 2:
                change_notifications()

if __name__ == "__main__":
    main()
