#!/usr/bin/pthon3
"""class Student that defines a student
"""


class Student:
    """student representation
    """

    def __init__(self, first_name, last_name, age):
        """init a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
