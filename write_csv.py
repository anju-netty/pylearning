#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import csv

with open ("people.csv","a+") as csvfile:
    writer = csv.writer(csvfile)
    csvdata = ("1", "Anju","34")
    writer.writerow(csvdata)

with open ( "people.csv", "r") as csvfile:
    csvfile.read()

with open ("numbers.csv","w+") as cf:
    writer = csv.writer(cf)
    writer.writerow(["x", "x+1", "x+2"])
    for x in range(1,5):
        writer.writerow([x, x+1, x+2])

