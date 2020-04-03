#
#print("\n\nHello welcome\n\n")
#
##open the file in read only mode
#f = open('configuration.txt','r')
#
##read one character from the file to the variable 'content'
#content = f.read(1)
#
##print content
#print(content)
#
##read 3 characters from the file to the variable 'content' from the current position
#content = f.read(3)
#print(content)
#
##this is find the current position of the pointer
#print("current position : ",f.tell())
#
##seek function will move the cursor to the 2 character in the file.
#print("move to position 2 now",f.seek(2))
#print(f.read(3))
#
#print(f.closed) #check if file is closed
#f.close() #close the file.
#

with open('configuration.txt','r') as file:
    print(file.read())



print(file.closed

