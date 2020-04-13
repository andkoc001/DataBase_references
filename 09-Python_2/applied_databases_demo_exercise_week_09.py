# Applied Databases, GMIT 2020
# Demo exercise 1 from week 09 lecture
# Author: Andrzej Kocielski
# ------------------------------


# -----
'''
Demo exercise 1

Import school.sql

Write a Python program that takes a number in from the console representing experience
and returns all details of all teachers whose experience is less than that number.

'''

# import external pieces of code from school.py file, being a child to this one
# school.py connects to SQL database and handles a query using functions get_experience()
import school


def get_number():
    return input("Enter number: ")


def main():

    while True:  # this is a 'forever' loop, unless interupted (break)

        # exeption handling
        try:

            #print("Show teachers with experience less than ...")
            number = int(get_number())

            # call funtion get_experience() from school.py, assign the results to 'teachers'
            teachers = school.get_experience(number)

            # print(teachers) # prints all the records that satisfy the query
            # for nice looking formating, records in a sequence one by one
            print("\nID", "\t|", "Name\t", "\t|", "Lev.",
                  "\t|", "Exp.", "\t|", "DOB")
            print("-"*52)
            for teacher in teachers:
                print(teacher["tid"], "\t|", teacher["Name"], "\t|", teacher["level"],
                      "\t|", teacher["experience"], "\t|", teacher["dob"])
            break

        # if invalid input (e.g. a letter) received
        except Exception as e:
            print("Invalid number, try again...")

    # test if I can change the query value, once the DB has been connected -> no, skipped
    # call the function get_experience() with hardwired parameter value
    # this would not make an effect - skipped - see the function definition
    school.get_experience(44)


# set a starting point for the program
# execute only if run as a script
if __name__ == "__main__":
    main()
