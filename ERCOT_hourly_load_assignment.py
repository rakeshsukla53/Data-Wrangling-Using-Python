__author__ = 'rsukla'

"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):",
    print sheet.cell_type(3, 2)
    print "Value in cell (row 0, col 1):",
    print sheet.cell_value(1, 1)

    max = sheet.cell_value(1, 1)
    min = sheet.cell_value(1, 1)
    sum = 0
    for i in range(1, sheet.nrows):
        if max < sheet.cell_value(i, 1):
            max = sheet.cell_value(i, 1)
            maxTime = sheet.cell_value(i, 0)

        if min > sheet.cell_value(i, 1):
            min = sheet.cell_value(i, 1)
            minTime = sheet.cell_value(i, 0)

        sum = sum + sheet.cell_value(i, 1)

    avg = sum / (sheet.nrows - 1)

    print "Maxinum value = %s , Mininum Value = %s and average = %s" %(max, min, avg)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)


    data = {
            'maxtime':  xlrd.xldate_as_tuple(maxTime, 0),
            'maxvalue': max,
            'mintime':  xlrd.xldate_as_tuple(minTime, 0),
            'minvalue': min,
            'avgcoast': avg
    }
    return data

def test():
    data = parse_file(datafile)
    print data
    #assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    #assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
