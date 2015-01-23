__author__ = 'rsukla'


# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!

# For creating array of dictionary

# weightMatrix = [{'A':0,'C':0,'G':0,'T':0} for k in range(motifWidth)]

'''
print line
            data = line.split(',')
            print data
            for i in range(0, 7):
                print data[i]
                headerInfo[data[i]] = ''
            break

    print headerInfo
'''
import os

DATADIR = os.getcwd()
DATAFILE = 'beatles-diskography.csv'
file_path = os.path.join(os.getcwd(), DATAFILE) #filepath to open

def parse_file(file_path):
    data = []
    with open(file_path, "rU") as f:
        i = 0
        k = 0

        for line in f:
            if k > 10:
                break
            if i == 0:
                headLine = line.split(',')
                i = i + 1
            else:
                elements = line.split(',')
                firstLine = {headLine[0]:elements[0], headLine[1]:elements[1], headLine[2]:elements[2],
                            headLine[3]:elements[3], headLine[4]:elements[4], headLine[5]:elements[5],
                            headLine[6].replace('\n', ''):elements[6].replace('\n', '')}

                data.append(firstLine)

            k = k + 1

        return data

def test():

    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    for i in range(0, len(d)):
        print d[i]


    #firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    #tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    #assert d[0] == firstline
    #assert d[9] == tenthline


test()