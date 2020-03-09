class Dog:
    #Class attributes
    species = "mammal"

    #Initialising attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #instance method
    def get_description(self):
        return " Name of the dog is {} and it is {} years old".format(self.name,self.age)
    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
class lambrador(Dog):
    #extending the functionalities of parent class 'Dog'
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class sausage(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,  speed)

# Child classes inherit attributes and
# behaviors from the parent class


jim = lambrador("Jim",5)
print(jim.get_description())
print(jim.run("fast"))

charlie = sausage("charlie",3)
print(charlie.get_description())
print(charlie.run("slow"))

julie = Dog("Julie", 8)
print(julie.get_description())

print("is Julie an instance of Dog",isinstance(julie,Dog))
print("is jim an instance of Dog",isinstance(jim,Dog))
print("is charlie an instance of Dog",isinstance(charlie,Dog))



    