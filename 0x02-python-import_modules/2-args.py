#!/usr/bin/python3
if __name__ == "__main__":
    import sys

"""Print the number of and list of arguments."""

arg_nums = len(sys.argv) - 1

if arg_nums == 0:
    print("0 arguments.")

elif arg_nums == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(arg_nums))

for i in range(1, arg_nums + 1):
    print(f"{i}: {sys.argv[i]}")
