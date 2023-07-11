#!/usr/bin/pthon3
"""class Student that defines a student by: (based on 9-student.py)
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
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
