#!/usr/bin/python3
import sys

"""Adds all arguments and prints the sum."""

args = sys.argv[1:]
int_args = [int(arg) for arg in args]
sum_args = sum(int_args)
print(sum_args)


if __name__ == "__main__":
    pass
