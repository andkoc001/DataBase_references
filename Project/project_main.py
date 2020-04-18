# Title: Applied Databases - Project
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie
# Description: Python program that facilitate work with mySQL and MongoDB databases.
# Context: Applied Databases, GMIT, 2020
# Lecturer: dr Gerard Harrison
#################################

# -------------
# Main function
# -------------


def main():
    '''
    This function defines a starting point for the program. It serves as a central hub and controls all other functionality of the program. it is called automatically at the program start.
    '''
    # Initialise array
    array = [4, 4, 25, 6, 1, 78, 0, 51]

    display_menu()

    while True:
        choice = input("Enter choice: ")

        if (choice == "1"):
            display_menu()
        elif (choice == "2"):
            display_menu()
        elif (choice == "3"):
            display_menu()
        elif (choice == "4"):
            display_menu()
        elif (choice == "5"):
            display_menu()
        elif (choice == "6"):
            display_menu()
        elif (choice == "7"):
            display_menu()
        elif (choice == ("x" or "X")):  # Exit condition
            break
        else:
            display_menu()


# ------------
# Display menu
# ------------
def display_menu():
    print("Applied Databases Project by Andrzej Kocielski, 2020")
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - View people")
    print("2 - View countries by independence year")
    print("3 - Add new person ")
    print("4 - View countries by name")
    print("5 - View countries by population")
    print("6 - Find students by address")
    print("7 - Add new course")
    print("x - Exit application")


# ------------------
# Check dependencies
# ------------------
if __name__ == "__main__":
    # execute only if run as a script
    main()
