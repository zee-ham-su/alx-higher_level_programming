#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}
