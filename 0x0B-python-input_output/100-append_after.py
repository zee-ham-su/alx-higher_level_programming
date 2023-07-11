#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    with open(filename, 'r+', encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string + "\n")
                break
        f.seek(0)
        f.writelines(lines)
