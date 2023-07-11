#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """ student representation
    """

    def __init__(self, first_name, last_name, age):
        """ init a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ acquire a dict representation of students
        """
        return self.__dict__
