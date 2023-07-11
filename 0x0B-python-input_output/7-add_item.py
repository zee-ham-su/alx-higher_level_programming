#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """creates an object from a “JSON file”"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
