#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import json
import sys


def save_to_json_file(items, filename):
    """Save the list of items to a file in JSON format.

    Args:
        items: The list of items to save.
        filename: The filename to save the items to.
    """

    with open(filename, "w") as f:
        json.dump(items, f)


def load_from_json_file(filename):
    """Load the list of items from a file in JSON format.

    Args:
        filename: The filename to load the items from.

    Returns:
        The list of items that were loaded from the file.
    """

    with open(filename, "r") as f:
        items = json.load(f)
    return items


def main():
    """Add all arguments to a Python list and save them to a file.
    """

    items = []
    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
