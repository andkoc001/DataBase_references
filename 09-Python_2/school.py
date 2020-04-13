import pymysql

# assume that initially there is no connection
conn = None

# connection to the database


def connect():
    global conn  # variable is global, so that it exists outside of the function
    conn = pymysql.connect(host="localhost",
                           user="ak-gmit",
                           password="Wro",  # enter the password here
                           db="school",
                           cursorclass=pymysql.cursors.DictCursor)


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

    # %s is a parameter that will be passed later (get_number()) to the cursor.execute()
    query = "SELECT * FROM teacher WHERE experience < %s"

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
