#!/usr/bin/python3
"""a class MyList that inherits from list
"""


class MyList(list):
    """ a class that inherits from a list"""

    def print_sorted(self):
        """
        Print the list in sorted order (ascending sort).
        """
        sorted_list = sorted(self)
        print(sorted_list)
