#######
-- MongoDB homework 2, week 07 (26/03/2020)
#######

## -- To start MongoDB from terminal
    mongod  ## let it run, and then in separate terminal
    mongo   ## in separate terminal in pararel to the previous command

## -- checking exising databases
    show dbs

############### Answers

##### -- 1. Import lab7.json to MongoDB.
## ans ##
    mongoimport --db <database_name> --collection <collection_name> --file <file_name>
    mongoimport --db lab --collection docs --file lab7.json


##### -- 2. Show the name and population of all cities where the population is over 10,000.
## ans ##
    db.lab7.find( {$and:[{city:{$exists:true}}, {pop:{$gt:10000}}]}, {_id:0, city:1, pop:1} )
alternatively
    db.lab7.find( {city:{$exists:true}, pop:{$gt:10000}}, {_id:0, city:1, pop:1} )


##### -- 3. Show the name and population of each state based on the cities shown (sum of cities populations groupped by state).
## ans ##
    db.lab7.aggregate([ {$match: {city:{$exists:true}}}, {$group: {_id: "$state", "Total pop":{$sum:"$pop"}}} ])
    

##### -- 4. Show the total population of cities in NY as “Population”.
## ans ##
    db.lab7.aggregate([ {$match: {state:"NY"}}, {$group: {_id: null, "Population":{$sum:"$pop"}}} ])
    db.lab7.aggregate([ {$match: {state:"NY"}}, {$group: {_id: null, "Population":{$sum:"$pop"}}}, {$project: {_id:0, "Population":1}} ])


##### -- 5. Show the _id, city and name of the capital city of each state for cities with a
population greater than 20,000.
## ans ##
    db.lab7.find( {$and:[{pop:{$gt:20000}}, {city:{$exists:true}}]}, {_id:1, "city":1, "capital.name":1} )

    

##### -- 6. Show all details for “Tom” including full details of his addresses.
## ans ##
    db.lab7.aggregate([ {$match:{name:"Tom"}}, {$lookup: {from:"lab7", localField: "addresses", foreignField:"_id", as:"lived in"} } ])

    

##### -- 7. Show all details for “Chesterfield” including full details of the state, but do not show details relating to its capital. HINT: Use the $project aggregation pipeline stage.
## ans ##
    db.lab7.aggregate([ {$match:{city:"CHESTERFIELD"}}, {$lookup: {from:"lab7", localField: "state", foreignField:"_id", as:"state"}}, {$project:{capital:0}} ])


   
## --------
Other exercises
## --------

##### -- 1. Import demo1.json to MongoDB.
## ans ##
    mongoimport --db demo --collection docs --file demo1.json

    show dbs
admin   0.000GB
config  0.000GB
demo    0.000GB
local   0.000GB
    use demo
switched to db demo
    db
demo
    show collections
docs
    db.docs.find({})
{ "_id" : "G00897678", "fname" : "Orla", "surname" : "McNicholas", "age" : 29, "sex" : "F" }
{ "_id" : "G00111222", "fname" : "Bill", "surname" : "Collins", "age" : 29, "sex" : "M" }
{ "_id" : "G00333588", "fname" : "Shane", "surname" : "Collins", "age" : 21, "sex" : "M" }
{ "_id" : "G00111444", "fname" : "Alice", "surname" : "Collins", "age" : 33, "sex" : "F" }
{ "_id" : "G00123488", "fname" : "Sean", "surname" : "Murphy" }
{ "_id" : "G00111555", "fname" : "Tom", "surname" : "Hughes", "age" : 21, "sex" : "M" }
{ "_id" : "G00111333", "fname" : "Bill", "surname" : "Murphy", "age" : 30, "sex" : "M" }
{ "_id" : "G00111789", "fname" : "Tom", "surname" : "McNamara", "age" : 21, "sex" : "M" }
{ "_id" : "G00123456", "fname" : "Mary", "surname" : "O'Neill", "age" : 23, "sex" : "F" }

##### -- 2. Show only the surname field of all documents
## ans ##
    db.docs.find({}, {_id:0, surname:1})


##### -- 3. Show only the fname and surname fields of all people aged 21 or older. Sort the results in ascending _surname_ and within surname on descending _fname_ order.
## ans ##
    db.docs.find({age:{$gte:21}} , {_id:0, fname:1, surname:1}).sort({surname:1, fname:-1})

    

##### -- 4. What is the name and type of index on the collection?
## ans ##
    db.docs.getIndexes()

    

##### -- 5. Show the combined age of everyone in the collection as "Total Age".
## ans ##
    db.docs.aggregate([ {$group:{_id:null, "Total Age":{$sum:"$age"}}} ])


##### -- 6. Show the combined age as "Total Age" and groupped by sex.
## ans ##    
    db.docs.aggregate([ {$group:{_id:"$sex", "Total Age":{$sum:"$age"}}} ])


##### -- 7. Import demo1a database (from bash, not mongo)
## ans ##
    mongoimport --db mydemo --collection docs2 --file demo1a.json
    


##### -- 8. Show the _registration_, _make_ and _model_ for all cars where the _bhp_ is over 115.
## ans ##
    db.docs2.find( {"engine.bhp":{$gt:115}}, {_id:1, make:1, model:1} )

    

##### -- 9. Show the average _bhp_ for each _make_ of car.
## ans ##
    db.docs2.aggregate([ {$group:{_id:"$make", average:{$avg:"$engine.bhp"}}} ])
    

##### -- 10. Import file demo1b
## ans ##
    mongoimport --db mydemo3 --collection docs3 --file demo1b.json

    
##### -- 11. Show the details of all books and for each book also show all details of the corresponding author as "Written By". Sort the results by author _name_.
## ans ##
    db.docs3.aggregate([ {$lookup: {from: "docs3", localField: "author", foreignField: "_id", as: "Written By"} }, {$sort:{"Written By.name":1}} ])




    
