#!/usr/bin/python3
"""
This module contains a function that adds two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either of the arguments is not an integer or a
        float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(-10, 10)
        0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
