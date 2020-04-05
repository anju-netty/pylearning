from stack_linkedlist import Stack


s1 = Stack()
s1.push(100)
s1.push(90)
s1.push(80)
s1.push(70)
s1.push(60)

print(s1.view_stack())
s2 = Stack()
s3 = Stack()
print(s1.size, s2.size,s3.size)

"""

starting is s1 is 5, peek = 60 , s2 = 0, s3 = 0

outcome : size s1 = 0, s2 = 0 , s3 = 5 (peek is 60)

"""

pop1 = s1.pop()
pop2 = s1.pop() 

s2.push(pop1)
s3.push(pop2)


print("S1 : {}  S2: {} S3 : {}".format( s1.view_stack(),s2.view_stack(),s3.view_stack()))


    

