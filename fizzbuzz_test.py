import unittest
from fizzbuzz import solve_fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_5(self):

        list_zz = solve_fizzbuzz(5)
        expected = "buzz"
        self.assertEqual(list_zz,expected)

    def test_solve_fizzbuzz_zero(self):
        
        with self.assertRaises(ValueError):
            solve_fizzbuzz(0)

    def test_multiple_of_3(self):

        list_zz = solve_fizzbuzz(9)
        expected = "fizz"
        self.assertEqual(list_zz,expected)

    def test_multiple_of_3_and_5(self):

        list_zz = solve_fizzbuzz(15)
        expected = "fizzbuzz"
        self.assertEqual(list_zz,expected)

    def test_not_multiple_of_3_and_5(self):

        list_zz = solve_fizzbuzz(4)
        expected = 4
        self.assertEqual(list_zz,expected)