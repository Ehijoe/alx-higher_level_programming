#!/usr/bin/python3
"""Print a list of integers."""


def print_list_integer(my_list=[]):
    """Print a list of integers."""
    for num in my_list:
        print("{:d}".format(num))
