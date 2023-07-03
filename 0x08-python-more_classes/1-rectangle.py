#!/usr/bin/python3
""" class that defines a rectangle
"""


class Rectangle:
    """A class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle object with given width and height."""
        self.__width = width
        self.__height = height

    def get_width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    def set_width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    def set_height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)
