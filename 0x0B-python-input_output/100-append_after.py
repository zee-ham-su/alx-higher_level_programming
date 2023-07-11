#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found"""
    lines = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            lines.append(line)
            if line.find(search_string) != -1:
                lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)
