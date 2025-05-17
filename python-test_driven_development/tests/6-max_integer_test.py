#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([9]), 9)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_all_same(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_string_list(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_single_string(self):
        self.assertEqual(max_integer("hello"), 'o')  # returns max char

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
