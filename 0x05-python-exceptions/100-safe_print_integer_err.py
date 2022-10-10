#!/usr/bin/python3
"""Safe Integer print with error message."""


def safe_print_integer_err(value):
    """Print an integer or display an error."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception:", err)
