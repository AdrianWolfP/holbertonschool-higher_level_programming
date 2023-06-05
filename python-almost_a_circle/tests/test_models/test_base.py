#!/usr/bin/python3
""" This module is a unittest for the base class """

import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """" test class for Base class """
    # setup and teardown methods are called before and after each test
    def setup(self):
        """ Reset the __nb__objects counter
        print test"""
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Base._base__nb_objects = 0

        self.base = Base()

    def tearDown(self):
        print("Base tearDown")

        sys.stdout = sys.__stdout__

        del self.base
        try:
            os.remove("Base.json")
        except FileNotError:
            pass

    def test_print(self):
        """ test print method """
        print("Hello, world!")
        self.assertEqual(self.capture_output.getvalue(), "Hello, world!\n")
        print("Hello, world!", file=sys.__stdout__)

        #test id assignment and if it increments correctly
        def test_id(self):
            """ Test__init__ method:
            id assigment in the Base class """
            self.assertEqual(self.base.id, 1)
            base2 = Base(50)
            self.assertEqual(base2.id, 50)
            base3 = Base()
            self.