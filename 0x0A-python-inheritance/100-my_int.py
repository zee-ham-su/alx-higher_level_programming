#!/usr/bin/python3
""" class MyInt that inherits from int:
"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, other):
        """
        Override the equality operator (==).
        Invert the behavior of the equality operator.
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=).
        Invert the behavior of the inequality operator.
        """
        return int(self) == int(other)
