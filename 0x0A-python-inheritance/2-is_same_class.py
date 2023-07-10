#!/usr/bin/python3
"""returns True if the object is exactly an instance of the
specified class. otherwise False
"""


def is_same_class(obj, a_class):
    """ return True if object is an instance """
    return type(obj) is a_class
