#!/usr/bin/python3
"""Integers division with debug."""


def safe_print_division(a, b):
    """Divide a by b."""
    ans = None
    try:
        ans = (a / b)
    except (TypeError, ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(ans))
    print("{} / {} = {}".format(a, b, ans))
    return ans
