#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text before each line containing a given string in
    a file
    """
    lines = []
    with open(filename) as file:
        for line in file:
            if search_string in line:
                lines.append(new_string)
            lines.append(line)

    with open(filename, "w") as file:
        file.writelines(lines)
