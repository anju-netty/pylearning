#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pickle 
from pprint import pprint as pprint

employee1 = {"Anju":[12,"Home",131],
            "Vivek":[4,"London",3435]
            }
employee2 = {"Vipul" : [23,"London",3434],
             "Deepika":[4,"Newyork",3435]
            }

employee =(employee1,employee2)
#print(employee)

# Below code wont work as Dictionary object cannot be serialised to be stored as a file object
#with open('employeefile.txt',w) as f:
#    f.write(employee)

#pickle module helps you to serialise and deserialise python objects to character stream be stored in a disk.

with open('employeefile','wb') as f:
    pickle.dump(employee,f)

with open('employeefile','rb') as f:
    deserialise_pyobj = pickle.load(f)

print(type(deserialise_pyobj))
pprint(deserialise_pyobj)


