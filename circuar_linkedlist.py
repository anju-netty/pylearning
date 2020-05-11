

class Node:

    def __init__(self, data, next_node):

        self.data = data
        self.next_node = next_node

def has_cycle(head_node):

    current_node = head_node

    previous_nodes_set = {current_node} #(a)

    while current_node.next_node!=None:
        x = current_node.next_node #if b is in (a) , c is in (a,b), is b in (a,b,c)
        if x in previous_nodes_set:
            #print("yes!")
            return "yes"
        else:
            current_node = current_node.next_node 
            previous_nodes_set.add(current_node) #(a,b), (a,b,c)
    
    return "No"

def had_cycle2(head_node):
    
    current_node = head_node
    pointer1 = current_node
    pointer2 = current_node.next_node

    while pointer1!=None and pointer2!=None:

        if pointer1 == pointer2:
            return True

        else:
            pointer1 = pointer1.next_node
            if pointer2.next_node == None:
                return False
            else:
                pointer2 = pointer2.next_node.next_node

    return False

        

if __name__ == "__main__":
    
    # a -> b <- -> c
    # a -> b -> c -> d
    #        <- ------       
   a = Node(5,None)
   b = Node(10,None)
   c = Node(20,None)

   a.next_node = b
   b.next_node = c
   c.next_node = None

   #print(has_cycle(a))
   print(had_cycle2(a))