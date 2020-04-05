import unittest
from queue_linkedlist import Queue

class TestQueue(unittest.TestCase):

    def test_enqueue(self):

        queue = Queue()
        queue.enqueue("Anju")
        queue.enqueue("Vivek")
        queue.enqueue("Aashna")

        head = queue.peek()
        expected = "Anju"
        print(head)
        self.assertEqual(head,expected)

    def test_enqueue_overflow(self):

        queue = Queue()
        queue.enqueue("Anju")
        queue.enqueue("Vivek")
        queue.enqueue("Aashna")
        queue.enqueue("Pooja")
        queue.enqueue("Preeti")
        queue.enqueue("vipul")
        queue.enqueue("deepika")
        
        head = queue.peek()
        expected = "Anju"
        
        self.assertEqual(head,expected)

    def test_dequeue(self):

        queue = Queue()
        queue.enqueue("Anju")
        queue.enqueue("Vivek")
        queue.enqueue("Aashna")
        queue.enqueue("Pooja")
        queue.enqueue("Preeti")

        queue.dequeue()
        result = queue.tail.data

        expected = "Pooja"

        self.assertEqual(expected,result)

    def test_dequeue_underflow(self):

        queue = Queue()
        queue.enqueue("Anju")
        queue.dequeue()
        queue.dequeue()

        result = queue.tail
        expected = None

        self.assertEqual(expected,result)

    def test_dequeue_head_tail(self):

        queue = Queue()
        queue.enqueue("Anju")

        queue.dequeue()
        result = queue.tail

        expected = None

        self.assertEqual(expected,result)