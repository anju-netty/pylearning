#!/Users/anju/Documents/anju/learning/dciv2-code/mycode3/bin/python

import pyttsx3

engine = pyttsx3.init()
fh = open("/Users/anju/Documents/anju/learning/dciv2-code/txttospeech.txt","r")


#contents = fh.read()
#engine.say(contents)
#print(contents)
#engine.runAndWait()

lines = fh.readlines()
for x in lines:
    engine.say(x)
    print(x)
    engine.runAndWait()
    
fh.close()
print("Thank you")
