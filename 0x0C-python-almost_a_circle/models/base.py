#!/usr/bin/python3
"""a base model class module
"""
import json


class Base:
    """" The base of all other classes to be created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init new base"""
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string"""
        if json_string is None or json_string == "[]":
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_inst = cls(1)
        else:
            dummy_inst = cls(1)
        dummy_inst.update(**dictionary)
        return dummy_inst
