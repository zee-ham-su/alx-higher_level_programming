#!/usr/bin/python3
"""a base model class module
"""
import json


class Base:
    """" The base of all other classes to be created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """inita new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))
