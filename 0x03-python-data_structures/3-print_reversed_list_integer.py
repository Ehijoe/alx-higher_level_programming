#!/usr/bin/python3
"""Print list in reverse."""


def print_reversed_list_integer(my_list=[]):
    """Print a list of integers in reverse."""
    for num in my_list[::-1]:
        print("{:d}".format(num))
