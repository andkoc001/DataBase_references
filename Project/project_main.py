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

# import proj20DB.py module, which connects to proj20DB.json database and handles queries
import proj20DB


# import pymysql library (a Python MySQL client) for the typical errors that may occur in pymysql library
import pymysql


# -------------
# Main function
# -------------

def main():
    '''
    This is the main function the program. It defines a starting point and controls all other functionality of the program. It is called automatically at the program start.
    '''

    print("\n\n>>> Applied Databases Project by Andrzej Kocielski, 2020 <<<")

    # Main menu screen
    display_menu()

    while True:  # this is a 'forever' loop, unless interupted (break)

        # Request input from the user, assign to variable choice
        choice = input("Enter your choice: ")

        if (choice == "1"):
            get_people()
            display_menu()

        elif (choice == "b"):
            get_people_b()
            display_menu()

        elif (choice == "2"):
            get_countries_by_ind_year()
            display_menu()

        elif (choice == "3"):
            add_new_person()
            display_menu()

        elif (choice == "4"):
            view_countries_by_name()
            display_menu()

        elif (choice == "5"):
            view_countries_by_population()
            display_menu()

        elif (choice == "6"):
            find_students_by_address()
            display_menu()

        elif (choice == "7"):
            add_new_course()
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
    This function makes connection to the world.sql database and returns all the details from the 'person' table, i.e. ID, name and age. Result is printed on the screen by two records at a time.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            print("\nID", "\t|", "Name\t", "\t|", "Age")
            print("-"*32)

            # call function view_people() from world.py; result is printed within the function
            world.view_people()
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong...", e)


# ---------------------------------------------------
# Choice 1b - view people from SQL database world.sql - another approach
# ---------------------------------------------------

def get_people_1b():
    '''
    This function makes connection to the world.sql database and returns all the details from the 'person' table, i.e. ID, name and age. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # call function view_people() from world.py; assign the results to 'rows'
            q = world.view_people_1b()

            while True:

                print("\nID", "\t|", "Name\t", "\t|", "Age")
                print("-"*30)

                # print out the records in chunks of two
                for chunk in chunks(q, 2):
                    for row in chunk:
                        print(row["personID"], "\t|",
                              row["personname"], "   \t|", row["age"])
                    x = input("Press Enter to continue or q to quit... ")
                    if (x == "q"):  # Exit condition
                        break

                # continue even if records are no more
                while True:
                    x = input("Press q to quit... ")
                    if (x == "q"):  # Exit condition
                        break
                break
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong, try again...", e)


# Code of this below function was taken from https://codereview.stackexchange.com/a/227539
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


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

            # get users input
            year = input("Enter year (q to exit): ")

            if (year == "q"):  # Exit condition
                break

            else:
                year = int(year)  # conver to a number

                # call function country_ind_year() from world.py; assign the results to 'rows'
                rows = world.country_ind_year(year)

                # print a table for a better legibility
                print("\nCountry", " |", "Continent",
                      " |", "Independence year")
                print("-"*41)

                # print all the records that satisfy the query in a loop row by row
                for row in rows:
                    print(row["Name"], " |",
                          row["Continent"], " |", row["IndepYear"])
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Invalid number, try again...\n")


# ----------------------------------------------------------------------
# Choice 3 - add a new and unique-named person to SQL database world.sql
# ----------------------------------------------------------------------

def add_new_person():
    '''
    This function requests the user to enter sequentially the name of the new person - the name must be unique - and the age. The function checks if a person with such a name exists in the database already, and if so, throws an error. The new person is added to the database with automatically assignes personID attribute - incremented by 1 from the largest exiting one.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # initialise variables and get user's input
            print("\nAdd new person (-1 to quit)")
            print("-"*27)
            new_name = input("Name: ")

            if new_name == "-1":
                break

            new_age = int(input("Age: "))  # conver to a number
            if new_age == -1:
                break

            # call function add_person() from world.py; assign the results to 'rows'
            world.add_person(new_name, new_age)

        # check if the new name already exists, then show a message
        except pymysql.err.IntegrityError as e:  # integrity error from pymysql library
            print("***Error:", new_name, "already exists.")

        except pymysql.err.ProgrammingError as e:  # programming error from pymysql library
            print("Programming Error: this table does not exist in the database.", e)

        except Exception as e:  # any other kind of error
            print("Invalid number, try again...\n")


# -----------------------------------------------------------------------------
# Choice 4 - view countries from SQL database world.sql by Name of part thereof
# -----------------------------------------------------------------------------

def view_countries_by_name():
    '''
    This function prompts the user to enter a country name or part of the name. Subsequently, it establishes connection to the world.sql database and returns all the countries, which names contain the entered string of characters. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # get users input
            name_or_part_thereof = input(
                "Enter country name or it's part (-1 to exit): ")

            if (name_or_part_thereof == "-1"):  # Exit condition
                break

            else:
                # rows = world.country_by_name(name_or_part_thereof)
                # add percent character (%) at the begining and end of the string
                rows = world.country_by_name("%"+name_or_part_thereof+"%")

                # print a table for a better legibility
                print("\nCountry", " |", "Continent",  " |", "Population",
                      " |", "Head of State")
                print("-"*54)

                # print all the records that satisfy the query in a loop row by row
                for row in rows:
                    print(row["Name"], " |", row["Continent"], " |",
                          row["Population"], " |", row["HeadOfState"])

            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong, try again...\n", e)


# -------------------------------------------------------------------
# Choice 5 - view countries from SQL database world.sql by population
# -------------------------------------------------------------------

def view_countries_by_population():
    '''
    This function first asks the user to choose between less than, greater than or equal operation followed by a prompt to enter population. Subsequently, it establishes connection to the world.sql database and returns all the countries, which satisfy the condition provided by the user. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # get users input
            print("\nCountries by population")
            print("-"*23)
            selection = input("Choose only from either '<', '>' or '=': ")

            if (selection not in ("<", ">", "=")):  # Exit condition
                break

            else:

                if selection == "<":

                    population = int(input("Enter population: "))

                    # call function country_by_pop_less_than() from world.py; assign the results to 'rows'
                    rows = world.country_by_pop_less_than(population)

                    # print a table for a better legibility
                    print("\nCode", " |", "Name",  " |",
                          "Continent",  " |", "Population")
                    print("-"*39)

                    # print all the records that satisfy the query in a loop row by row
                    for row in rows:
                        print(row["Code"], "  |", row["Name"], " |",
                              row["Continent"], " |", row["Population"])

                if selection == ">":

                    population = int(input("Enter population: "))

                    # call function country_by_pop_greater_than() from world.py; assign the results to 'rows'
                    rows = world.country_by_pop_greater_than(population)

                    # print a table for a better legibility
                    print("\nCode", " |", "Name",  " |",
                          "Continent",  " |", "Population")
                    print("-"*39)

                    # print all the records that satisfy the query in a loop row by row
                    for row in rows:
                        print(row["Code"], "  |", row["Name"], " |",
                              row["Continent"], " |", row["Population"])

                if selection == "=":

                    population = int(input("Enter population: "))

                    # call function country_by_pop_equal() from world.py; assign the results to 'rows'
                    rows = world.country_by_pop_equal(population)

                    # print a table for a better legibility
                    print("\nCode", " |", "Name",  " |",
                          "Continent",  " |", "Population")
                    print("-"*39)

                    # print all the records that satisfy the query in a loop row by row
                    for row in rows:
                        print(row["Code"], "  |", row["Name"], " |",
                              row["Continent"], " |", row["Population"])

            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong, try again...\n")


# -----------------------------------------------------------------------
# Choice 6 - find students by address from mongoDB database proj20DB.json
# -----------------------------------------------------------------------

def find_students_by_address():
    '''
    This function requests the user to enter a city. Next, it makes connection to the proj20DB.json database and returns details of students who live in the city. Result is printed on the screen.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # get user's input
            print("\nFind student by city (-1 to quit)")
            print("-"*33)
            city = input("Enter City: ")

            if city == "-1":
                break

            # concatonate the city name
            # city = "\""+city+"\""

            # call function find_by_city() from proj20DB.py
            rows = proj20DB.find_by_city(city)
            # rows = proj20DB.find_b(city) # alternative approach - not 100% satisfactory

            # print a table for a better legibility
            print("\nStudentID", " |", "Name",  " |",
                  "Age",  " |", "Qualifications")
            print("-"*38)

            # print all the records that satisfy the query in a loop row by row
            for item in rows:

                # conditional choice - if there are three elements in the item (id, details, qualifications), print them out
                if (len(item)) > 2:
                    print(item["_id"], " |", item["details"]["name"], " |",
                          item["details"]["age"], " |", item["qualifications"])
                else:
                    print(item["_id"], " |", item["details"]
                          ["name"], " |", item["details"]["age"])

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Something went wrong, try again...\n")

# -------------------------------------------------------------
# Choice 7 - add a new course to mongoDB database proj20DB.json
# -------------------------------------------------------------


def add_new_course():
    '''
    The user is asked to enter the following information describing a course: _id, Name, Level. Next, the function makes connection to the proj20DB.json database, and the provided information will be subsequently inserted into the database. However, in case the user enters _id of an existing course, relevant error message is shown.
    '''

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            # get user's input
            print("\nAdd new course (-1 to quit)")
            print("---------------------------")

            new_course_id = (input("_id: "))
            if new_course_id == "":
                print("Error: _id cannot be empty")
                break
            elif new_course_id == "-1":
                break
            new_course_id = new_course_id.upper()  # convert to all upper case

            new_course_name = (input("Name: "))
            if new_course_name == "-1":
                break

            # exit condition
            new_course_level = int((input("Level: ")))
            if new_course_level == "-1":
                break

            # call function insert_course() from proj20DB.py
            proj20DB.insert_course(
                new_course_id, new_course_name, new_course_level)

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Error: course level must be a number, try again... (-1 to quit)\n")


# ------------
# Display menu
# ------------

def display_menu():

    print("")
    print("MENU")
    print("=" * 4)
    print("1 - View people (world.sql)")
    # print("1b - View people - different approach, but imperfect (world.sql)")
    print("2 - View countries by independence year (world.sql)")
    print("3 - Add new person (world.sql)")
    print("4 - View countries by name (world.sql)")
    print("5 - View countries by population (world.sql)")
    print("6 - Find students by address (proj20DB.json)")
    print("7 - Add new course (proj20DB.json)")
    print("\nx - Exit application\n")


# ------------------
# Check dependencies
# ------------------
if __name__ == "__main__":
    # execute only if run as a script
    main()
