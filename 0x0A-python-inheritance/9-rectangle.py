#!/usr/bin/python3
"""
Rectangle class definition
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: The rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
