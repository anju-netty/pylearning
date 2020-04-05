
class Node:

    def __init__(self, data, next_node):

        self.data = data
        self.next_node = next_node
       

class Stack:

    def __init__(self, data, limit):
        #first instance of the stack will be head and its tail both
        self.head = Node(data,None)
        self.limit = limit
        self.size = 1

    def push(self,data):
        #inserting at the beginning

        if self.size < self.limit:
            new_node = Node(data, self.head)
            self.head = new_node
            self.size = self.size + 1
        else:
            print("Stack is full!")

    def peek(self):
        #top of the stack
        return self.head.data

    def pop(self):
        #from the top
        if self.size != 0:
            print("Popping head ", self.head.data)
            self.head = self.head.next_node
            self.size = self.size - 1
        else:
            print("Stack is empty!")
     
    def view_stack(self):

        stack_list = []
        if self.size != 0:
            current_node = self.head
            
            while current_node!=None:
                #print(current_node.data)
                stack_list.append(current_node.data)
                current_node = current_node.next_node

        return stack_list
        