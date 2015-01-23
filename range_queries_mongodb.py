__author__ = 'rsukla'

#!/usr/bin/env python
""" Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""
from datetime import datetime

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def range_query():
    # You can use datetime(year, month, day) to specify date in the query
    query = {"foundingDate" : { "$gte" : datetime(2001, 1, 1), "$lt" : datetime(2100, 12, 31)} }
    return query

#all the cities that were founded on 21st centuary


if __name__ == "__main__":

    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint
    pprint.pprint(cities[0])


'''
21st centuary means 2001 is the start date of the countries


It began on January 1, 2001, and will end on December 31, 2100

'''



'''
inequality operator
Mongodb provides variety of inequality operator and dollar sign $ precedes them everytime

$gt  # Greater than
$lt  # Less than
$gte  # Greater than equal to
$lte  # Less than equal to
$ne  # not equal to

query = {"population" : { "$sgt" : 250000}}  # If you want population greater than 250000

{"foundingDate" : { "$gte" : datetime(2001, 1, 1}, "$lte" : datetime(2100, 12, 31} }

client = Mongoclient('\mongodb://localhost : 27017')

db = client.examples

def find()

    query = {"population" : {"$gt" :  250000}}

    cities = db.cities.find(query)

    num_cities = 0
    for c in citiies:
        pprint.pprint(c)
        num_cities = + 1
'''



