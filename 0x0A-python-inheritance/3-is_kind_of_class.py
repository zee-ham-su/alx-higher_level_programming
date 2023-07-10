#!/usr/bin/python3
"""function that Check if the object is an instance of the
specified class or its inherited classes
"""


def is_kind_of_class(obj, a_class):
    """  returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the
    specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
