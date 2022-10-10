#!/usr/bin/python3
"""Print an integer safely."""


def safe_print_integer(value):
    """Print an integer safely."""
    try:
        print("{:d}", value)
    except ValueError:
        return False
    return True
