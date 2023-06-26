#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        converted_value = int(value)
        print("{:d}".format(converted_value))
        return True
    except ValueError:
        type_name = type(value).__name__
        error_message = (
            "Exception: Unknown format code 'd' for object of type '{}'"
        )
        print(error_message.format(type_name), file=sys.stderr)
        return False
