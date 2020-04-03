class Node:

    def __init__(self, value, next_node = None):

        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    
class Linkedlist:

    def __init__(self, value=None):
        self.headnode = Node(value)

    def get_head_node(self):
        return self.headnode

    def insert_beginning(self,new_value):

        new_node = Node(new_value)
        new_node.set_next_node(self.headnode)
        self.headnode = new_node

    def stringify(self):

        stringlist = ""

        current_node = self.get_head_node()

        while current_node:

            if(current_node.get_value() != None):
                stringlist = stringlist + str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()

        return stringlist

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
          self.head_node = current_node.get_next_node()
        else:
          while current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
              current_node.set_next_node(next_node.get_next_node())
              #use break if you wish to remove the first occurrence of a given value.
              #break 

            else:
              current_node = next_node

ll = Linkedlist(5)
ll.insert_beginning(10)
ll.insert_beginning(20)
ll.insert_beginning(20)
ll.insert_beginning(40)


print(ll.stringify())

ll.remove_node(20)

print(ll.stringify())

