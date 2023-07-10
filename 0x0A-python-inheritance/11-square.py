#!/usr/bin/python3
"""
Square class definition
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.
        Returns:
            str: The square description.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
