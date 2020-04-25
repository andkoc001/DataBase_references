# This file is an external file (a child) of the project_main.py file.
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie
# Description: This script facilitates work with SQL database - world.sql.
# Context: Applied Databases, GMIT, 2020
# Lecturer: dr Gerard Harrison
##################################


# -----------------------
# Import external modules
# -----------------------


# pymysql library - a Python MongoDB client
import pymongo


# ----------------------------------------
# Establish connection to the sql database
# ----------------------------------------


# assume that initially there is no connection
myclient = None


# define function connecting to the database

def connect():
    global myclient
    # print("1: ", myclient)
    myclient = pymongo.MongoClient()
    # print("2: ", myclient)
    myclient.admin.command('ismaster')


# ----------------------------------------------------------------------------
# User choice 6 - find students by address from mongoDB database proj20DB.json
# ----------------------------------------------------------------------------


def find_by_city(city_name):

    # check if there is connection already, i.e. conn != None,
    # then make a connection, using function connect()
    if (not myclient):
        # print("Initialising connection to database...")
        connect()
        # print("Connected")

    # otherwise state that the connection already exists
    else:
        # print("Already connected to database")
        pass

    mydb = myclient["proj20DB"]  # name of the database
    docs = mydb["docs"]  # name of the collection inside square brackets

    # --------------------------------------
    # specify the mongoDB filter (aka query)
    # Important! attribute name must be inside quotes, otherwise python consider it a variable
    # my_query_mongo_pipeline = [{"$match": {"details.address": city_name}, {"$lookup": {"from": "docs", "localField": "qualifications", "foreignField": "_id", "as": "qualifications"}}]

    # projections (what data to be shown)
    proj = {"_id": 1, "details.name": 1, "details.age": 1, "qualifications": 1}

    # pipeline
    pipel = [{"$match": {"details.address": city_name}}, {"$project": proj}]
    # --------------------------------------

    # execute the query
    r6 = docs.aggregate(pipeline=pipel)

    return r6


# -----------------------------------------------------------------------------
# User choice 6b - find students by address from mongoDB database proj20DB.json
# -----------------------------------------------------------------------------
# another approach - not 100% functional as expected

def find_b(city_name):

    # check if there is connection already, i.e. conn != None,
    # then make a connection, using function connect()
    if (not myclient):
        # print("Initialising connection to database...")
        connect()
        # print("Connected")

    # otherwise state that the connection already exists
    else:
        # print("Already connected to database")
        pass

    mydb = myclient["proj20DB"]  # name of the database
    docs = mydb["docs"]  # name of the collection inside square brackets

    # filter aka mongo query
    # Important! attribute name must be in inside quotes, otherwise python consider it a variable
    my_query_mongo_find = {"details.address": city_name}

    # projections (what data to be shown)
    proj = {"_id": 1, "details.name": 1, "details.age": 1,
            "qualifications": {"$exists": "True"}}

    # execute the query
    findings = docs.find(filter=my_query_mongo_find, projection=proj)

    # print out the result
    for item in findings:
        # print(item)
        print(item["_id"], "|", item["details"]["name"], "|",
              item["details"]["age"])  # , "|", item["qualifications"])


# -------------------------------------------------------------
# Choice 7 - add a new course to mongoDB database proj20DB.json
# -------------------------------------------------------------

def insert_course(new_course_id, new_course_name, new_course_level):

    # check if there is connection already, i.e. conn != None,
    # then make a connection, using function connect()
    if (not myclient):
        # print("Initialising connection to database...")
        connect()
        # print("Connected")

    # otherwise state that the connection already exists
    else:
        # print("Already connected to database")
        pass

    mydb = myclient["proj20DB"]
    docs = mydb["docs"]  # name of the collection inside square brackets

    try:

        # create an array
        new_course_details = [
            {"_id": new_course_id, "name": new_course_name, "level": new_course_level}]

        # execute mongo insert command
        docs.insert_many(new_course_details)

        print("Course details have been added: ", new_course_details)

    except Exception as e:
        print("*** Error: _id", new_course_id, "already exists.")
