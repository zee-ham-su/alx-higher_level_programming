#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found"""
    def append_after(filename="", search_string="", new_string=""):
        lines = []
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                lines.append(line)
            if search_string in line:
                lines.append(new_string)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write("".join(lines))
