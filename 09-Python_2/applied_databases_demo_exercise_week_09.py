# Applied Databases, GMIT 2020
# Demo exercise from week 09 lecture
# Author: Andrzej Kocielski
# ------------------------------


# -----
'''
Demo exercise

Import school.sql

Write a Python program that takes a number in from the console representing experience
and returns all details of all teachers whose experience is less than that number.

Write a Python program that asks to entrer details of a new subject and adds it to
the database.
'''

# import external pieces of code from school.py file
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


# set a starting point for the program
# execute only if run as a script
if __name__ == "__main__":
    main()
