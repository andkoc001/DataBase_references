# This file is an external file (a child) of the project_main.py file.
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie
# Description: This script facilitates work with SQL database - world.sql.
# Context: Applied Databases, GMIT, 2020
# Lecturer: dr Gerard Harrison
##################################

# -----------------------
# Import external modules
# -----------------------

# pymysql library - a Python MySQL client
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
                           user="",  # enter your user name here !!!
                           password="",  # enter the password here !!!
                           db="world",
                           cursorclass=pymysql.cursors.DictCursor)


# --------------------------------------------------------
# User choice #1 - define functions that perform SQL query
# --------------------------------------------------------

# show all the people


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

        # execute the cursor
        cursor.execute(my_query_sql)

        # Looping over the results of fetchmany()
        while True:
            rows = cursor.fetchmany(2)
            for row in rows:
                print(row["personID"], "\t|",
                      row["personname"], "   \t|", row["age"])
            x = input("Press Enter to continue or q to quit... ")
            # if (x == "q"):  # Exit condition
            #    break
            if (not row) or (x == "q"):
                break

    # conn.close()
    # return the result to the calling funtion in project_main.py


# --------------------------------------------------------
# User choice #1b - define functions that perform SQL query
# --------------------------------------------------------

# show all the people - an alternative approache, but with bugs

def view_people_b():

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

        # execute the cursor
        cursor.execute(my_query_sql)

        # assign the results to a variable
        r1 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r1


# --------------------------------------------------------
# User choice #2 - define functions that perform SQL query
# --------------------------------------------------------

# show all the people
# as argument is passed the year of independence
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

        # execute the cursor
        cursor.execute(my_query_sql, year)

        # assign the results to a variable
        r2 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r2


# ----------------------------------------------------------
# User choice #3 - define functions that perform SQL command
# ----------------------------------------------------------

# add a new person to the person table
# as argumenta are passed the name and age of the new person
def add_person(n_name, n_age):

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
    my_query_sql = "INSERT INTO person (personname, age) VALUES (%s, %s)"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        cursor.execute(my_query_sql, (n_name, n_age))


# --------------------------------------------------------
# User choice #4 - define functions that perform SQL query
# --------------------------------------------------------

# show countries by name
# as argument is passed a country name or part thereof
def country_by_name(name_part):

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
    my_query_sql = "SELECT Name, Continent, Population, HeadOfState FROM country WHERE Name LIKE %s"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        cursor.execute(my_query_sql, (name_part))

        # assign the results to a variable
        r4 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r4


# --------------------------------------------------------
# User choice #5 - define functions that perform SQL query
# --------------------------------------------------------

# show countries that population is less than specified in the argument
# as argument is population of a country
def country_by_pop_less_than(pop):

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
    my_query_sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population < %s"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        cursor.execute(my_query_sql, (pop))

        # assign the results to a variable
        r51 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r51


# show countries that population is greater than specified in the argument
# as argument is population of a country
def country_by_pop_greater_than(pop):

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
    my_query_sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population > %s"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        cursor.execute(my_query_sql, (pop))

        # assign the results to a variable
        r52 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r52


# show countries that population is equal to specified in the argument
# as argument is population of a country
def country_by_pop_equal(pop):

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
    my_query_sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population = %s"
    # ------------------------------------------------

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        cursor.execute(my_query_sql, (pop))

        # assign the results to a variable
        r53 = cursor.fetchall()

        # return the result to the calling funtion in project_main.py
        return r53
