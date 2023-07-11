#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""


import sys
from collections import Counter


def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("Total file size:", size)
    for code, count in sorted(status_codes.items()):
        print(code + ":", count)


lines = []
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        lines.append(line.strip().split(" "))

        if line_count % 10 == 0:
            size = sum(int(line[-1]) for line in lines)
            status_codes = Counter(line[-2] for line in lines
                                   if line[-2] in valid_codes)
            print_stats(size, status_codes)
            lines = []

except KeyboardInterrupt:
    size = sum(int(line[-1]) for line in lines)
    status_codes = Counter(line[-2] for line in lines if line[-2]
                           in valid_codes)
    print_stats(size, status_codes)
