#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class Sqaure"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = None

    def __str__(self):
        """String representation of the Square instance.

        Returns:
        str: The string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """retrieve the size of square"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the size value of square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
