#!/Users/anju/Documents/anju/learning/dciv2-code/mycode3/bin/python

#pyttsx3 is a text-to-speech conversion library in Python. 
#Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

import pyttsx3

engine = pyttsx3.init() # object creation

#open the text file in read mode
fh = open("/Users/anju/Documents/anju/gitpycodes/pylearning/txttospeech.txt","r")

#save the lines in a list to read the file line by line
lines = fh.readlines()

#to parse through the list and say the lines loud
for x in lines:
    engine.say(x)
    print(x)
    engine.runAndWait()

#close the file    
fh.close()
print("Thank you")
