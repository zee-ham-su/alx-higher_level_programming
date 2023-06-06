#!/usr/bin/python3
output_str = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        output_str += chr(i)
    else:
        output_str += chr(i - 32)

print(output_str, end="")
