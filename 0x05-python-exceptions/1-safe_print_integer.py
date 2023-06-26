#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        exception_types = {ValueError: False, TypeError: False}
        return exception_types.get(type(e), True)
