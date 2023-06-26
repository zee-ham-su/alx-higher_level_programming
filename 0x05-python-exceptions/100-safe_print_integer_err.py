#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True
    except ValueError:
        print("Exception: Value is not an integer", file=sys.stderr)
        return False
