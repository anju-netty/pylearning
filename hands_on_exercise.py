"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("Type of pi is {} and value of pi is {}".format(type(pi),pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50 :
    print(i," is less than 50")
elif i > 50:
    print(i," is greater than 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print("You picked fruit ",picked_fruit)
if picked_fruit == "orange":
    print("color of {} is Orange".format(picked_fruit))
elif picked_fruit == "strawberry":
    print("color of {} is Red".format(picked_fruit))
elif picked_fruit == "banana":
    print("color of {} is Yellow".format(picked_fruit))
else:
    print("no color")



# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiply(num1,num2):
    return num1 * num2

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiply(12,96))

print("48 x 17 =",multiply(48,17))

print("196523 x 87323 =",multiply(196523,87323))
