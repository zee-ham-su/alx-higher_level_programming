#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import os.path


def add_items(filename, *args):
    """Add all arguments to a Python list and save them to a file.
    """

    items = []
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            items = json.load(f)
    for arg in args:
        items.append(arg)

    with open(filename, "w") as f:
        json.dump(items, f)


if __name__ == "__main__":
    add_items("add_item.json", "item1", "item2", "item3")
