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
        """String representation of the Rectangle instance.

        Returns:
        str: The string representation of the Rectangle instance.
        """

        return "[Sqaure] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y,
                                                 self.width)
