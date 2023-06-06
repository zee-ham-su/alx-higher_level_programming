#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        value = c
    elif c > b:
        value = a + b
    else:
        value = a * b - c

    return value
