
name = input("Enter string : ")

temp = name[len(name)-1]
#5 4 3 2 1 0


for i in range(len(name)-2,-1,-1):
    
    temp = temp + name[i]

print(temp)
