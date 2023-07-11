#!/usr/bin/python3
"""function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """load an object from a json file
    Args:
         filename: name of the file to load
    returns:
        object: the deserialized object
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
