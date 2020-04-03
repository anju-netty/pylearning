#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import csv
from pprint import pprint as pprint

def stats(nodeid, value):

    return()

num_of_rows = 0

# To read the stats file
with open("stats.txt",'r') as csvfile: 
    reader = csv.reader(csvfile,delimiter=',')

#configlist is a list of lists, each row in reader is a list which has detail of one device    
    configlist = []
    
    for row in reader:
        configlist.append(row)
        num_of_rows = num_of_rows + 1 # count the number of rows

pprint(configlist)

valuelist = []     
total = 0

for row in range(num_of_rows-1):
    item = configlist[row][1]
    total=total+int(item)
    valuelist.append(configlist[row][1])

stats = [min(valuelist), max(valuelist), total/num_of_rows]

with open ("analysis.csv","a+") as cf:
    writer = csv.writer(cf,delimiter=",")
    writer.writerow(stats)


print("Min : {} Max : {} Avg : {}".format(min(valuelist),max(valuelist),total/num_of_rows))

