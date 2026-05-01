# IsoLogic: Infection Prevention Isolation & PPE Quick Guide
# This program helps users select an infectious condition and receive
# recommended isolation precautions, PPE, and cleaning reminders.


# IsoLogic: Infection Prevention Isolation & PPE Quick Guide
# This program helps users select an infectious condition and receive
# recommended isolation precautions, PPE, and cleaning reminders.


def get_precaution(condition):
    # Dictionary stores infection guidance based on the user's menu selection
    precautions = {
        "1": {
            "name": "C. difficile",
            "isolation": "Contact Precautions",
            "ppe": "Gloves and gown",
            "notes": "Wash hands with soap and water. Use bleach-based cleaning products."
        },
        "2": {
            "name": "Influenza",
            "isolation": "Droplet Precautions",
            "ppe": "Surgical mask",
            "notes": "Place patient in a private room if possible. Limit transport."
        },
        "3": {
            "name": "COVID-19",
            "isolation": "Droplet/Contact Precautions",
            "ppe": "Mask, gloves, gown, and eye protection",
            "notes": "Follow facility respiratory protection guidance."
        },
        "4": {
            "name": "Tuberculosis",
            "isolation": "Airborne Precautions",
            "ppe": "N95 respirator",
            "notes": "Negative pressure room is required. Keep door closed."
        },
        "5": {
            "name": "MRSA",
            "isolation": "Contact Precautions",
            "ppe": "Gloves and gown",
            "notes": "Use good hand hygiene and keep wounds covered."
        },
        "6": {
            "name": "RSV",
            "isolation": "Droplet/Contact Precautions",
            "ppe": "Mask, gloves, and gown",
            "notes": "Use precautions based on symptoms and facility policy."
        }
    }

    # Returns the selected condition details if valid; otherwise returns None
    return precautions.get(condition)


def display_menu():
    # Displays the infection menu for the user
    print("\n===== IsoLogic: Infection Prevention Quick Guide =====")
    print("Select a condition below:")
    print("1. C. difficile")
    print("2. Influenza")
    print("3. COVID-19")
    print("4. Tuberculosis")
    print("5. MRSA")
    print("6. RSV")
    print("Q. Quit")


def print_report(result):
    # Prints a formatted isolation and PPE report
    print("\n========== MINI ISOLATION SIGN ==========")
    print("Condition: ", result["name"])
    print("Isolation: ", result["isolation"])
    print("PPE:       ", result["ppe"])
    print("Notes:     ", result["notes"])
    print("=========================================")


def ask_run_again():
    # Asks the user if they want to repeat the program
    while True:
        again = input("\nRun program again? (yes/no): ").strip().lower()

        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Invalid input. Please type yes or no.")


def main():
    # Main program loop
    while True:
        display_menu()

        try:
            # Gets the user's menu selection
            choice = input("Select an option: ").strip()
        except Exception:
            print("Error reading input. Please try again.")
            continue

        # Allows the user to quit from the main menu
        if choice.lower() == "q":
            print("Program ended.")
            break

        # Retrieves the precaution information based on user selection
        result = get_precaution(choice)

        # Validates input and prints the report if the selection is valid
        if result:
            print_report(result)

            # Matches the flowchart decision: Run Again?
            if not ask_run_again():
                print("Program ended.")
                break
        else:
            print("Invalid input. Please select a number from the menu or Q to quit.")


# Starts the program
main()