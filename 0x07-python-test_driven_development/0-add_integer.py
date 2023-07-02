#!/usr/bin/python3
"""
This module contains a function that adds two integers.

"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as an integer.

    Args:
        a: The first number.
        b: The second number. Defaults to 98.

    Returns:
        int: The sum of 'a' and 'b' as an integer.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
