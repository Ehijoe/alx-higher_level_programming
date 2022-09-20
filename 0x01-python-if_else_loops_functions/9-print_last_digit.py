#!/usr/bin/python3
"""Print the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of a number."""
    digit = str(number)[-1]
    print(digit, end="")
    return digit
