class Dog:
    #Class attribute
    species = "mammal"

    #Initializer/Instance attributes
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def description(self):
        return("Dog\'s name is {} and it is {} years old".format(self.name,self.age))

    def speak(self, sound):
        return("{} says {}".format(self.name,sound))

#Determine the oldest dog      
def get_biggestdog(*args):
    return max(args)


#Initiating the Dog object 
philo = Dog("Philo",6)
Rocky = Dog("Rocky",3)

#Access the instance attributes
print("{} is {} and {} is {}".format(
    philo.name,philo.age,Rocky.name,Rocky.age))

#if philo.species == "mammal":
#    print("{0} is a {1}!".format(philo.name,philo.species))

print("The biggest dog is {}".format(get_biggestdog(philo.age,Rocky.age)))

print(philo.description(),"\n",philo.speak("Woof Woof!"))