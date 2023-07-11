#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ prints what is in a text file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
