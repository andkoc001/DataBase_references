# This file is an external file (a child) of the project_main.py file.
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie
# Description: This script facilitates work with SQL database - world.sql.
# Context: Applied Databases, GMIT, 2020
# Lecturer: dr Gerard Harrison
##################################

# -----------------------
# Import external modules
# -----------------------

# import pymysql library - a Python MySQL client
import pymysql


# ----------------------------------------
# Establish connection to the sql database
# ----------------------------------------

# assume that initially there is no connection
conn = None


# define function connecting to the database
def connect():
    global conn  # variable is global, so that it exists outside of the function
    conn = pymysql.connect(host="localhost",
                           user="ak-gmit",
                           password="Wro",  # enter the password here !!!
                           db="world",
                           cursorclass=pymysql.cursors.DictCursor)


# --------------------------------------------------------
# User choice #1 - define functions that perform SQL query
# --------------------------------------------------------

# show all the people
# as argument
def view_people():

    # check if there is connection already, i.e. conn != None,
    # then make a connection, using function connect()
    if (not conn):
        print("Initialising connection to database...")
        connect()
        print("Connected")

    # otherwise state that the connection already exists
    else:
        print("Already connected to database")

    # ------------------------------------------------
    # specify the SQL query assigned to 'my_query_sql'
    my_query_sql = "SELECT * FROM person"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor, assign results to variable 'y'
        cursor.execute(my_query_sql)

        # assign the results to a variable
        r1 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r1


# --------------------------------------------------------
# User choice #2 - define functions that perform SQL query
# --------------------------------------------------------

# show all the people
# as argument
def country_ind_year(year):

    # check if there is connection already, i.e. conn != None,
    # then make a connection, using function connect()
    if (not conn):
        print("Initialising connection to database...")
        connect()
        print("Connected")

    # otherwise state that the connection already exists
    else:
        print("Already connected to database")

    # ------------------------------------------------
    # specify the SQL query assigned to 'my_query_sql'
    my_query_sql = "SELECT Name, Continent, IndepYear FROM country WHERE IndepYear = %s"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor, assign results to variable 'y'
        cursor.execute(my_query_sql, year)

        # assign the results to a variable
        r2 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r2
