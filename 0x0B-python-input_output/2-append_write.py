#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ function that appends a text file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_num = file.write(text)
    return char_num
