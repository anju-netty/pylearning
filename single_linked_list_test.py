import unittest
from single_linked_list import Node, LinkedList

class TestSingleLinkedList(unittest.TestCase):

    def test_validdata(self):
        
        ll = LinkedList(5)
        ll.append_node(6)
        ll.append_node(10)
        ll.append_node(20)
        result_ll = ll.get_linkedlist()
        actual_list = [5,6,10,20]
        self.assertEqual(result_ll,actual_list)

    def test_insert_node_in_the_begining(self):

        ll = LinkedList(5)
        ll.append_node(6)
        ll.append_node(10)
        ll.append_node(20)
        
        ll.insert_node_in_the_begining(7)
        
        result_ll = ll.get_linkedlist()
        actual_list = [7,5,6,10,20]
        self.assertEqual(result_ll,actual_list)

    def test_delete_node(self):

        ll = LinkedList(5)
        ll.append_node(6)
        ll.append_node(10)
        ll.append_node(20)

        ll.delete_node(6)

        result_ll = ll.get_linkedlist()
        actual_list = [5,10,20]
        self.assertEqual(result_ll,actual_list)

    def test_delete_head_node(self):


        ll = LinkedList(5)
        ll.append_node(6)
        ll.append_node(10)
        ll.append_node(20)

        ll.delete_node(5)

        result_ll = ll.get_linkedlist()
        actual_list = [6,10,20]
        self.assertEqual(result_ll,actual_list)

    def test_delete_last_node(self):


        ll = LinkedList(5)
        ll.append_node(6)
        ll.append_node(10)
        ll.append_node(20)
        
        ll.delete_node(20)

        result_ll = ll.get_linkedlist()
        actual_list = [5,6,10]
        self.assertEqual(result_ll,actual_list)