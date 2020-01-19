#!/Users/anju/Documents/anju/learning/dciv2-code/mycode3/bin/python

import pyttsx3

engine = pyttsx3.init()

greeting = "Hello My name is Anto! I am an Alien"
print(greeting)
engine.say(greeting)
engine.runAndWait()

question =  ["What is your name? ","Lovely name!","How old are you?","You are super cute"]
engine.say(question[0])
answer = input(question[0])
engine.runAndWait()

statement = answer + " you have a " + question[1]
print( statement)
engine.say(statement)
engine.runAndWait()
    


