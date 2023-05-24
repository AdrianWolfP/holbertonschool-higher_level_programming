#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function
    """
    def test_max_integer(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_at_beginning(self):
        test_list = [4, 1, 3, 2]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_in_the_middle(self):
        test_list = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(test_list), 5)

    def test_one_neg_number(self):
        test_list = [-1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_only_neg_numbers(self):
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_element(self):
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)