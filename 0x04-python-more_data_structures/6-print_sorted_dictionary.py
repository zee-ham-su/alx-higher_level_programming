#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_keys_list = sorted(a_dictionary.keys())
    for key in sorted_keys_list:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
