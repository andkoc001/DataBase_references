# This file relates to (is a child of) applied_databases_demo_exercise_week_09.py

# import pymysql library - a Python MySQL client
import pymysql

# assume that initially there is no connection
conn = None

# connection to the database


def connect():
    global conn  # variable is global, so that it exists outside of the function
    conn = pymysql.connect(host="localhost",
                           user="ak-gmit",
                           password="",  # enter the password here
                           db="school",
                           cursorclass=pymysql.cursors.DictCursor)


# define a function that performs a SQL query
# the query is to show all the teachers with years of experience less than specified
def get_experience(number):

    # check if there is connection, i.e. conn != None,
    # than make a connection, using function connect()
    if (not conn):
        print("Initialising connection...")
        connect()
        print("Connected")

    # otherwise state that the connection already exists
    else:
        print("Already connected")

    # specify the SQL query
    # %s is a parameter that will be passed later (get_number()) to the cursor.execute()
    query = "SELECT * FROM teacher WHERE experience < %s"

    # connect to the SQL database and perform the query; return the found records
    with conn:

        # create the cursor
        cursor = conn.cursor()

        # execute the cursor
        # number is the value of %s parameter from the query
        cursor.execute(query, (number))

        # assign the results to a variable
        x = cursor.fetchall()

        # print(x) # for testing

        return x
