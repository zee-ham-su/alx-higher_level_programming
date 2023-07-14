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
