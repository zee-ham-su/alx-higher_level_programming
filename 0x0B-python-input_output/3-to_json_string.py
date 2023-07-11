#!/usr/bin/python3
""" function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)
    Args:
        my_obj: The object to be serialized into JSON.

    Returns:
        A JSON-formatted string representing the serialized object.
    """
    return json.dumps(my_obj)
