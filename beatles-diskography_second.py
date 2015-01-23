__author__ = 'rsukla'

'''
Now to solve the same problem, we will be using csv module
'''

import os
import csv
import pprint

DATADIR = os.getcwd()
DATAFILE = 'beatles-diskography.csv'
file_path = os.path.join(os.getcwd(), DATAFILE) #filepath to open

def parse_file(file_path):
    data = []
    with open(file_path, "rb") as f:
        f = csv.DictReader(f)  ## create a dictionary , apapne aap header ke saath values aa jayenge
        for line in f:
            print line   ## Apane aap assume karta hain ki first line will be header and then proceed accordingly
        return data
def test():

    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    #for i in range(0, len(d)):
    #    print d[i]

test()

'''
the program beatles-diskography.py is solved in few lines using csv module and DictReader functionality


import csv



if we use DictReader then we won't be requiring it to convert into a dictionary since we are already doing i

with open(file_name, 'rb') as f:
        r = csv.DictReader(f)
        for line in r:
            data.append(r)
        return data

'''

#csv.DictReader it will give you the values in dictionary




