#!/usr/bin/python3

""" This module writes Base class """

import json
class Base:
   
    """ Base class is base of all other classes.
    Should be able to manage id attribute in all your future classes and to avoid duplicating of the same code """
    __nb_object = 0

    def __init__(self, id=None):
        """ class constructor for Base class with 
        optional id attribute that is set to none by default, if id is not, assign public instance
        Args:
        id (int, optional): public instance attribute . Defaults to None.
        if ID is NULL then increment """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = ID
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """" Static method that returns the json string """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """ Static method that Returns: list of json string """
        if not json_string:
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method wrties json """
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        # convert list object to list of dictionaries
        list_dicts = [obj.to_dictionary () for obj in list_objs]
        # coverts list dictionaries to json string
        json_str = cls.to_json_string(list_dicts)
        #write the JSON string to a file
        with open(filename, "w") as file:
            file.write(json_str)
        
    @classmethod
    def create(cls, **dictionary):
        """ Class method """
        # create a dummy instance for cls to be created
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = clas(1)
        # update the dummy instance with the dictionary
        dummy.update(**dictionary)
        #created instance of the class with all atters set
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """ Class method that returns """
        #create a class name JSON file
        filename = cls.__name__ + ".json"
        # try to open file
        try:
            with open(filename, "r") as file:
                # read the file and convert to list of dic
                list_dicts = cls.from_json_string(file.read())
                # convert list of dic to list of incstances
                return [cls.create(**dictionary) for dictionary in list_dicts]
            # if empty file or file does not exist return empty list
            except FileNotFoundError:
                return []