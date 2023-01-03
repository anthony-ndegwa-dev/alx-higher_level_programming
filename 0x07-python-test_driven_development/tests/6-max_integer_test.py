#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    """ Tests for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_repeated_number(self):
        self.assertEqual(max_integer([70, 70, 70]), 70)

    def test_float_numbers(self):
        self.assertEqual(max_integer([2.73, 6.33, -9.123, 17.4, 6.3]), 17.4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 8, 7, 6, 5]), 9)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_zero_number(self):
         self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-70, -45, -12, -3]), -3)

    def test_one_number_list(self):
        self.assertEqual(max_integer([6]), 6)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([6, '9'])

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(5)

if __name__ == "__main__":
    unittest.main()
