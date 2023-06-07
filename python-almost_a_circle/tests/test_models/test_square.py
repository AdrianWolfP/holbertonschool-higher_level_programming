#!/usr/bin/python3
''' Unittest for class Square '''
import unittest
import json
from models.square import Square


class TestSquamples(unittest.TestCase):
    ''' Unittest for class Square '''

    def test_simple_squample(self):
        squample = Square(7)
        self.assertEqual(squample.size, 7)

    def test_squample_with_x(self):
        squample = Square(13, 37)
        self.assertEqual(squample.size, 13)
        self.assertEqual(squample.x, 37)
    
    def test_squample_with_args(self):
        squample = Square(13, 3, 7)
        self.assertEqual(squample.size, 13)
        self.assertEqual(squample.x, 3)
        self.assertEqual(squample.y, 7)

    def test_squample_string_size(self):
        with self.assertRaises(TypeError):
            squample = Square("13", 3, 7, 89)

    def test_squample_string_x(self):
        with self.assertRaises(TypeError):
            squample = Square(13, "3", 7, 89)
    
    def test_squample_string_y(self):
        with self.assertRaises(TypeError):
            squample = Square(13, 3, "7", 89)

    def test_squample_negative_size(self):
        with self.assertRaises(ValueError):
            squample = Square(-13, 3, 7, 89)
    
    def test_squample_negative_x(self):
        with self.assertRaises(ValueError):
            squample = Square(13, -3, 7, 89)
    
    def test_squample_negative_y(self):
        with self.assertRaises(ValueError):
            squample = Square(13, 3, -7, 89)
    
    def test_squample_zero_size(self):
        with self.assertRaises(ValueError):
            squample = Square(0, 3, 7, 89)
    
    def test_squample_str_function(self):
        squample = Square(13, 3, 7, 89)
        self.assertEqual(squample.__str__(), "[Square] (89) 3/7 - 13")
    
    def test_squample_to_dictionary(self):
        squample = Square(13, 3, 7, 89)
        self.assertEqual(squample.to_dictionary(), {'id': 89, 'size': 13, 'x': 3, 'y': 7})
    
    def test_squample_update_args(self):
        squample = Square(10, 10, 10, 10)
        squample.update(13, 3, 7, 89)
        self.assertEqual(squample.__str__(), "[Square] (13) 7/89 - 3")
    
    def test_squample_update_kwargs(self):
        squample = Square(10, 10, 10, 10)
        squample.update(size=13, x=3, y=7, id=89)
        self.assertEqual(squample.__str__(), "[Square] (89) 3/7 - 13")
    
    def test_squample_area(self):
        squample = Square(13, 3, 7, 89)
        self.assertEqual(squample.area(), 169)
    
    def test_squample_create(self):
        squample = Square.create(**{'id': 89, 'size': 13, 'x': 3, 'y': 7})
        self.assertEqual(squample.size, 13)
        self.assertEqual(squample.x, 3)
        self.assertEqual(squample.y, 7)
        self.assertEqual(squample.id, 89)

    def test_squample_load_from_file(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_save_to_file_empty(self):
        squample = Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()