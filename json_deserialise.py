import json

#deserialising json into a python obj
with open('friends.json','rt') as f:
    obj = json.load(f)
    #print(type(obj))
    #print(obj)

#declaring a json string
json_string = {"Anju":("Chelms",34,"Home"), "Vivek":["Lon",35,"Office"]}

#Serialising python dict dump_string to text file /json file 

dump_string = json.dumps(json_string, indent = 4)
print(dump_string)

with open("friends1.json", 'wt') as f:
    json.dump(dump_string, f, indent = 4)





