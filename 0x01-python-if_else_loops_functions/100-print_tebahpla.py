#!/usr/bin/python3
def print_ascii_alphabet_in_reverse():
    for i in range(122, 96, -1):
        if i % 2 == 0:
            print(chr(i).lower(), end="")
        else:
            print(chr(i).upper(), end="")


print_ascii_alphabet_in_reverse()
