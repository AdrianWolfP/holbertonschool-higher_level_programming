#!/usr/bin/python3
''' Unittest for integer_validator '''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' Unittest for to_json_string method '''

    def test_to_json_string_empty(self):
        json_string = ''
        list_input = Base.to_json_string(json_string)
        list_output = '[]'
        self.assertEqual(list_input, list_output)
    
    def test_to_json_string_None(self):
        json_string = None
        list_input = Base.to_json_string(json_string)
        list_output = '[]'
        self.assertEqual(list_input, list_output)

    def test__init__id(self):
        Base._Base__nb_objects = 0
        r1 = Base(10)
        self.assertEqual(r1.id, 10)

    def test__init__id_None(self):
        Base._Base__nb_objects = 0
        r1 = Base(None)
        self.assertEqual(r1.id, 1)
    
    def test__init__id_more(self):
        Base._Base__nb_objects = 0
        r1 = Base(10)
        r2 = Base(7)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 7)
    
    def test__init__id_None_more(self):
        Base._Base__nb_objects = 0
        r1 = Base(None)
        r2 = Base(None)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_from_json_string(self):
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}]'
        list_input = Base.from_json_string(json_string)
        list_output = [{'id': 89, 'width': 10, 'height': 4},
                          {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_empty(self):
        json_string = ''
        list_input = Base.from_json_string(json_string)
        list_output = []
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_None(self):
        json_string = None
        list_input = Base.from_json_string(json_string)
        list_output = []
        self.assertEqual(list_input, list_output)

if __name__ == '__main__':
    unittest.main()