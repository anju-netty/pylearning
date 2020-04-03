#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import csv #standard module to parse through csv file
import pprint as pp #
with open('airtravel.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]

    #pp.pprint(year_1958)

    max_year1958 = max(year_1958.values())

    for k,v in year_1958.items():
        if max_year1958 == v:
            print(f'Busiest month in year 1958 is {k} , Flights : {v}')

    
            
    