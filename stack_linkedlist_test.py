import unittest
import stack_linkedlist

class TestStackLinkedList(unittest.TestCase):

    def test_push_to_sack(self):

        stack = stack_linkedlist.Stack()
        stack.push(10)
        stack.push(20)
        stack.push(50)
        stack.push(50)
        stack.push(50)
        stack.push(50)
        stack.push(50)
        stack.push(50)
        

        result = stack.view_stack()
        print(result)
        expected = [50,50,50,20,10]
        self.assertEqual(result,expected)

    def test_peek_sack(self):

        stack = stack_linkedlist.Stack()
        stack.push(5)
        stack.push(1)

        result = stack.peek()
        expected = 1
        self.assertEqual(result,expected)

    def test_pop(self):

        stack = stack_linkedlist.Stack()
        stack.push(5)
        stack.push(4)
        stack.push(1)

        stack.pop()
    
        result = stack.view_stack()
        print(result)
        expected = [4,5]
        self.assertEqual(result,expected)

    def test_pop_empty(self):

        stack = stack_linkedlist.Stack()
        stack.push(5)
        stack.push(4)
        stack.push(1)

        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
     
        result = stack.view_stack()
        print(result)
        expected = []
        self.assertEqual(result,expected)
