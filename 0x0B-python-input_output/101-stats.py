#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("File size:", size)
    for code in sorted(status_codes):
        print(code + ":", status_codes[code])


lines = []
valid_codes = ['200', '401', '403', '404', '405', '500']
line_count = 0
status_codes = {}

try:
    for line in sys.stdin:
        line_count += 1
        lines.append(line.strip().split(" "))

        if line_count % 10 == 0:
            size = sum(int(line[-1]) for line in lines)
            for line in lines:
                if line[-2] in valid_codes:
                    if line[-2] not in status_codes:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            print_stats(size, status_codes)
            lines = []

except KeyboardInterrupt:
    size = sum(int(line[-1]) for line in lines)
    for line in lines:
        if line[-2] in valid_codes:
            if line[-2] not in status_codes:
                status_codes[line[-2]] = 1
            else:
                status_codes[line[-2]] += 1
    print_stats(size, status_codes)
