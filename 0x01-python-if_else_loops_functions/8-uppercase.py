#!/usr/bin/python3
"""Print a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end="")
    print()
