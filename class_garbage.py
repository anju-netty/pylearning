"""
Python (like many other languages) will detect that an object is no longer being used 
and perform what is called “garbage collection”. During the process, unused objects are 
released to free up resources. When a variable is assigned to an instance and then assigned
to a different instance, the prior assignment will be a candidate for “garbage collection” 
provided that no other variable is pointing to it. The following code example shows that the 
instance originally assigned to my_obj is destroyed when the variable is assigned to a new instance.
"""

class TestClass:

    #Methods that are used to prepare an object being instantiated are called constructors.
    def __init__(self, id):
        self.id = id
        print("Creating object id = " + str(self.id))

    def __del__(self):
        print("Deleting object id = " + str(self.id))

print("Instantiating object 1")
my_obj = TestClass(1)

print("Instantiating object 2")
my_obj2 = TestClass(2)

print("Instantiating object 3")
my_obj = TestClass(3)

print("Instantiating object 4")
my_obj = TestClass(4)

# Wait for 10 seconds to show that object 1 is destroyed before the program ends
from time import sleep
sleep(10)