# Title: Applied Databases - Project
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie
# Description: Python program that facilitate work with mySQL and MongoDB databases. The application is based on the lecture materials, and other sources quoted as they were used in the program.
# Context: Applied Databases, GMIT, 2020
# Lecturer: dr Gerard Harrison
####################################


# -------------------------------------
# Import external modules and databases
# -------------------------------------

# import world.py module, which connects to world.sql database and handles queries
import world


# -------------
# Main function
# -------------


def main():
    '''
    This function defines a starting point for the program. It serves as a central hub and controls all other functionality of the program. it is called automatically at the program start.
    '''

    print("\n\n>>> Applied Databases Project by Andrzej Kocielski, 2020 <<<")

    display_menu()

    while True:  # this is a 'forever' loop, unless interupted (break)

        # Request input from the user, assign to variable choice
        choice = input("Enter your choice: ")

        if (choice == "1"):
            get_people()
            display_menu()
        elif (choice == "2"):
            get_countries_by_ind_year()
            display_menu()
        elif (choice == "3"):
            get_year()  # for testing only
            display_menu()
        elif (choice == "4"):
            display_menu()
        elif (choice == "5"):
            display_menu()
        elif (choice == "6"):
            display_menu()
        elif (choice == "7"):
            display_menu()
        elif (choice == "x"):  # Exit condition
            break
        else:
            display_menu()


# --------------------------------------------------
# Choice 1 - view people from SQL database world.sql
# --------------------------------------------------

def get_people():
    '''
    This function makes connection to the world.sql database and returns all the details from the 'person' table, i.e. ID, name and age. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # call funtion view_people() from world.py; assign the results to 'rows'
            rows = world.view_people()

            # print(teachers) # prints all the records that satisfy the query
            # for nice looking formating, records in a sequence one by one
            print("\nID", "\t|", "Name\t", "\t|", "Age")
            print("-"*32)
            for row in rows:
                print(row["personID"], "\t|",
                      row["personname"], "   \t|", row["age"])
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong, try again...")


# --------------------------------------------------------------------------
# Choice 2 - view countries from SQL database world.sql by Independence Year
# --------------------------------------------------------------------------

def get_countries_by_ind_year():
    '''
    This function requests the user to enter a year. Next, it makes connection to the world.sql database and returns all the countries, which became independent in that year. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            #print("Show teachers with experience less than ...")
            # another function is used here
            year = input("Enter year or press 0 to exit: ")
            if (year == "0"):  # Exit condition
                break
            else:
                year = int(year)

                # call funtion country-ind_year() from world.py; assign the results to 'rows'
                rows = world.country_ind_year(year)

                # print(teachers) # prints all the records that satisfy the query
                # for nice looking formating, records in a sequence one by one
                print("Countries by independence year")
                print("\nCountry", " \t|", "Continent",
                      "\t|", "Independence year")
                print("-"*52)
                for row in rows:
                    print(row["Name"], "  \t|",
                          row["Continent"], " \t|", row["IndepYear"])
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Invalid number, try again...\n")


# auxiliary function
def get_year():
    '''
    This function is typically called from within get_countries_by_ind_year() function. It returns a string, which will be later used in formulating a SQL query.
    '''
    print("Countries by independence year")
    print("------------------------------")
    return input("Enter year of independence: ")

# ------------
# Display menu
# ------------


def display_menu():
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
