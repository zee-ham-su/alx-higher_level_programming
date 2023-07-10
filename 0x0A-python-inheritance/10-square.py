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
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
