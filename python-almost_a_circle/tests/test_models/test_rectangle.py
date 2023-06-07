#!/usr/bin/python3
''' Unittest for class Base '''
import sys
import json
import io
from unittest.mock import patch
from contextlib import redirect_stdout
import unittest
from models.rectangle import Rectangle

class TestTangles(unittest.TestCase):
    ''' Unittest for class Rectangle '''

    def test_simple_tangle(self):
        testangle = Rectangle(13, 37)
        self.assertEqual(testangle.width, 13)
        self.assertEqual(testangle.height, 37)
    
    def test_tangle_with_args(self):
        testangle = Rectangle(1, 3, 3, 7, 89)
        self.assertEqual(testangle.width, 1)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_string_height(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle("1", 3, 3, 7, 89)
    
    def test_tangle_string_width(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, "3", 3, 7, 89)
    
    def test_tangle_string_x(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, "3", 7, 89)
    
    def test_tangle_string_y(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, 3, "7", 89)
    
    def test_tangle_negative_height(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(13, -37)
    
    def test_tangle_negative_width(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(-13, 37)
    
    def test_tangle_negative_x(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, -3, 7, 89)
    
    def test_tangle_negative_y(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, 3, -7, 89)
    
    def test_tangle_zero_height(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(0, 37)
    
    def test_tangle_zero_width(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(13, 0)

    def test_tangle_str_function(self):
        testangle = Rectangle(3, 7, 1, 3, 89)
        self.assertEqual(testangle.__str__(), "[Rectangle] (89) 1/3 - 3/7")
    
    def test_tangle_to_dictionary(self):
        testangle = Rectangle(1, 3, 3, 7, 89)
        self.assertEqual(testangle.to_dictionary(), {'x': 3, 'y': 7, 'id': 89, 'height': 3, 'width': 1})
    
    def test_tangle_update(self):
        testangle = Rectangle(1, 2, 3, 4, 5)
        testangle.update(1, 3, 3, 7, 89)
        self.assertEqual(testangle.width, 3)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 7)
        self.assertEqual(testangle.y, 89)
        self.assertEqual(testangle.id, 1)
    
    def test_tangle_update_kwargs(self):
        testangle = Rectangle(1, 2, 3, 4, 5)
        testangle.update(height=1, width=3, x=3, y=7, id=89)
        self.assertEqual(testangle.width, 3)
        self.assertEqual(testangle.height, 1)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_area(self):
        testangle = Rectangle(3, 2)
        self.assertEqual(testangle.area(), 6)

    def test_tangle_create(self):
        testangle = Rectangle.create(**{'x': 3, 'y': 7, 'id': 89, 'height': 3, 'width': 1})
        self.assertEqual(testangle.width, 1)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_load_from_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_tangle_display(self):
        testangle = Rectangle(2, 3, 1, 1)
        expected_output = "\n" \
                            " ##\n" \
                            " ##\n" \
                            " ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            testangle.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_tangle_display_without_y(self):
        testangle = Rectangle(2, 3, 1, 0)
        expected_output = " ##\n" \
                            " ##\n" \
                            " ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            testangle.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_tangle_display_without_x_and_y(self):
        testangle = Rectangle(2, 3, 0, 0)
        expected_output = "##\n" \
                            "##\n" \
                            "##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            testangle.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()