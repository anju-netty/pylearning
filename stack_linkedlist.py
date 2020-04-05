"""
Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.

alt text

The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

    Only one disk can be moved at a time.
    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    No disk may be placed on top of a smaller disk.


"""

class Node:

    def __init__(self, data, next_node):

        self.data = data
        self.next_node = next_node

class Stack:

    def __init__(self):
        #first instance of the stack will be topitem and its tail both
        self.topitem = None
        self.limit = 5
        self.size = 0

    def is_empty(self):

        return self.size <= 0

    def has_space(self):

        return self.size < self.limit

    def push(self,data):
        #inserting at the beginning

        if self.has_space():
            new_node = Node(data, self.topitem)
            self.topitem = new_node
            self.size = self.size + 1
        else:
            print("Stack is full!")

    def peek(self):
        #top of the stack
        return self.topitem.data

    def pop(self):
        
        if not self.is_empty():

            print("Popping topitem ", self.topitem.data)
            popped = self.topitem.data
            self.topitem = self.topitem.next_node
            self.size = self.size - 1
            return popped
         
        else:
            print("Stack is empty!")
            return None
     
    def view_stack(self):

        stack_list = []
        if self.size != 0:
            current_node = self.topitem
            
            while current_node!=None:
                #print(current_node.data)
                stack_list.append(current_node.data)
                current_node = current_node.next_node

        return stack_list

        


    