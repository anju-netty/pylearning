#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import csv

#with open('passwd.csv', 'r') as f:
#    reader = csv.reader(f, delimiter = ':', lineterminator = '\n')
#    for row in reader:
#        print(row)
#
#print(csv.list_dialects())

csv.register_dialect('hashes',delimiter='#',quoting=csv.QUOTE_NONE,lineterminator='\n')



with open('items.csv','w+') as csvfile:
    writer = csv.writer(csvfile,dialect='hashes')
    writer.writerow(('meat',6,2.0))

#with open('items.csv', 'r') as csvfile:
#    reader = csv.reader(csvfile,dialect='hashes')
#    for row in reader:
#        print(row)