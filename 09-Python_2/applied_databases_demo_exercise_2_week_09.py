# Applied Databases, GMIT 2020
# Demo exercise 2 from week 09 lecture
# Author: Andrzej Kocielski
# ------------------------------


# -----
'''
Demo exercise 2

Import school.sql

Write a Python program that asks to entrer details of a new subject and adds it to
the database.

'''
# -----

# import external pieces of code from school_2.py file, being a child to this one
# school_2.py connects to SQL database and updates db using function add_subject()
import school_2

# import import pymysql library - a Python MySQL client
# for the typical errors that occurs in pymysql library
import pymysql


def main():

    # initialise variables
    name = input("Enter subject: ")
    teacher = input("Enter teacher: ")
    l_cert = input("Is on Leaving Certificate [1/0]: ")

    # exeption handling
    # check if the correct data is entered by user
    try:
        school_2.add_subject(name, teacher, l_cert)

    # check if the subject (which is the primary key) already exists, then show a message
    except pymysql.err.IntegrityError as e:  # from pymysql library
        print("Error,", name, "already exists.")
    except pymysql.err.ProgrammingError as e:  # from pymysql library
        print("Error: this table does not exist in the database.")
        print("Programming Error:", e)
    except Exception as e:  # any other kind of error
        print("Error: ", e)


# set a starting point for the program
# execute only if run as a script
if __name__ == "__main__":
    main()
