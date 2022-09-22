#!/usr/bin/python3
"""Find the sum of arguments."""

import sys

if __name__ == '__main__':
    sum_ = 0
    for num in sys.argv[1:]:
        sum_ += int(num)
    print(sum_)
