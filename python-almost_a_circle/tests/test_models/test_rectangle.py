#!/usr/bin/python3
""" Unittest for class Rectangle """
import unittest
import sys
import io
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestTangles(unittest. TestCase):
""" Unittest for class Rectagnle """
    def setup(self):
        """Set up test method"""
        print("Rectangle setUp")
        
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output