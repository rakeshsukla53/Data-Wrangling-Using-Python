__author__ = 'rsukla'

from pymongo import MongoClient   #Mongoclient is the real class jiske through tu call kar sakta hain
import pprint

client = MongoClient('mongodb://localhost:27017/')

db = client.examples

porsche = {
	        "layout" : "rear mid-engine rear-wheel-drive layout",
	        "name" : "Porsche Boxster",
	        "productionYears": [ ],
	        "modelYears": [ ],
	        "bodyStyle": "roadster",
	        "assembly": [
		    "Finland",
		    "Germany",
		    "Stuttgart",
		    "Uusikaupunki"
	                    ],
	        "class" :"sports car",
	        "manufacturer" : "Porsche"
}

#db.autos.insert(porsche)  #we are using the insert command here  # insert karsakta hain

#for a in db.autos.find():
#    pprint.pprint(a) # print that document out

def find():  #if you want to see more specific values in your database then you can print out this as well
    search = db.autos.find({'manufacturer':'Porsche'}, {'bodyStyle': 'roadster'})   # we can find the element here
    for a in search:                                  # bahut baar insert ho gaya hain table mein
        pprint.pprint(a)  # print out mar sakta hain database

find()

'''
Python App / PyMongo will send a request to the MongoDB database. The request will come
in BSON form.


from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')  #this is the default port number

#mongodb://localhost:27017/ here we specify the connection string


db = client.examples
db.autos.insert(tesla_s)   # insert document here

for a in db.autos.find():  # find karna hain documents
    pprint.pprint(a)

ab agar data database se kuch find out karna hain toh

from pymongo import MongoClient
import pprint

db = client.examples

def find():
    autos = db.autos.find({ "manufactuer" : "toyota"})
    for a in autos:
        pprint.pprint(a)

if __name__ == '__main__':
    find()
'''




