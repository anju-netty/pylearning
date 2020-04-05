class Node:

    def __init__(self,data, next_node):
        self.data = data
        self.next_node = next_node

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.limit = 5
        
    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size <= 0
    
    def enqueue(self,data):

        if self.has_space():

            if self.is_empty():
                self.head = Node(data,None)
                self.tail = self.head
                self.size = self.size + 1

            else:
                new_node = Node(data,None)
                self.tail.next_node = new_node
                self.tail = new_node
                self.size = self.size + 1
        else:

            print("Queue is full!")
    
    def dequeue(self):

        if not self.is_empty():
            #print("\n\n\nPopping ", self.tail.data)
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.size = self.size - 1
            else:
                current = self.head
                while current.next_node != self.tail:
                    current = current.next_node
                current.next_node = None
                self.tail = current
                self.size = self.size - 1
        else:
            print("Queue is empty!")


    def peek(self):

        if not self.is_empty():
            return self.head.data
        else:
            return None



