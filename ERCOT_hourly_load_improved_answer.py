

'''

We can easily solve the issue of using excel sheets here by using sheet functionality

def parse_file(datafile):

        workbook = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)

        data = [[sheet.cell_value(r,col) for col in range(sheet.ncols)]for r in range(nrows)]
        cv = sheet.col.values(1, start_rowx = 1, end_rowx = None)
        maxval = max(cv)
        minval = min(cv)

        maxpos = cv.index(maxval) + 1
        minpos = cv.index(minval) + 1

        maxtime = sheet.cell_value(maxpos, 0)
        realmaxtime = xlrd.xldate_as_tuple(maxtime, 0)
        mintime = sheet.cell_value(minpos, 0)
        realmintime= xlrd.xldate_as_tuple(mintime, 0)


this is a much better solution of the previous problem. It takes less time and obviously

and also pprint module helps to print the value in a more concise way

'''

