#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print(int(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return False
    return True
