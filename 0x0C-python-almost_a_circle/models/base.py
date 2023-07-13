#!/usr/bin/python3
"""a base model class module
"""


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
