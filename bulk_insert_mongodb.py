from autos import process_file


def insert_autos(infile, db):
    autos = process_file(infile)

    for a in autos:
        db.autos.insert(a)
    # Your code here. Insert the data in one command
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'


if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print db.autos.find_one()

'''
Now if you want to insert data into mongodb here is the code. And if you want to check how many data you have inserted
then you need to use the count function

client = MongoClient('mongodb://localhost:27017')
db = client.examples

num_autos = db.myautos.find().count()
print 'num_autos before', num_autos

for a in autos:
    db.myautos.insert(a)

num_autos = db.myautos.find().count() # if you want to count and check how many line you have inserted
print "num_autos after", num_autos

'''


