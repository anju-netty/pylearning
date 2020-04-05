#!usr/bin/env/ python3

class Node:

    def __init__(self, data, next_node):
    
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self, data):

        print("Initialising head")
        self.head = Node(5, None)
    
    def __del__(self):

        print("deleting node")

    def append_node(self, new_node_data):

        new_node = Node(new_node_data,None)
        current_node = self.head

        while current_node.next_node != None:
            print("updatting currnet node {} with next node {}".format(current_node.data,current_node.next_node.data))
            current_node = current_node.next_node

        current_node.next_node = new_node
    
    def insert_node_in_the_begining(self, data):
      new_node = Node(data,None)
      new_node.next_node = self.head
      self.head = new_node

    
    def get_linkedlist(self):

        current_node = self.head
        linkedlist = []
        while True:
            linkedlist.append(current_node.data)
            if current_node.next_node != None:
                current_node = current_node.next_node
            else:
                break
        
        return linkedlist

  
    def delete_node(self, data):
        
        current_node = self.head

        if current_node.data == data: #to delete head node
                self.head = current_node.next_node

        else:

            while current_node.next_node!= None:

                if current_node.next_node.data == data:
                    if current_node.next_node.next_node == None:
                        current_node.next_node = None
                        break
                    else:
                        current_node.next_node = current_node.next_node.next_node
                        break
                else:
                    current_node = current_node.next_node



