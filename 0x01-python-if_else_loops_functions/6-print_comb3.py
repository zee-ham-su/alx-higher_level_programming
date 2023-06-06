#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x != y:
            print("{:02d}".format(x * 10 + y), end="")
            if x != 8 or y != 9:
                print(",", end="")

print()
