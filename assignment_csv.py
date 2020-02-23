#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import csv

num_of_rows = 0

# To read the text file into csv file and the delimiter is ':'
with open("devices.txt",'r') as csvfile: 
    reader = csv.reader(csvfile,delimiter=':')

#configlist is a list of lists, each row in reader is a list which has detail of one device    
    configlist = []
    
    for row in reader:
        configlist.append(row)
        num_of_rows = num_of_rows + 1 # count the number of rows

with open ("devicelist.csv","w+") as cf:
    writer = csv.writer(cf,delimiter=",",)
    writer.writerow(["Device Name", "Ipadress", "Username", "Password"]) #Title of columns
    for x in range(num_of_rows):
        col = []
        for y in range(4): 
            #For loop to traverse through the column. If I use configlist[x][y] directly use in writer
            #it will write every item in a different line.
            col.append(configlist[x][y]) 
        writer.writerow(col) #this is a row