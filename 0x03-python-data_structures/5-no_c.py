#!/usr/bin/python3
def no_c(my_string):
    modified_string = ""
    for i in range(len(my_string)):
        if my_string[i] not in "cC":
            modified_string += my_string[i]

    return modified_string
