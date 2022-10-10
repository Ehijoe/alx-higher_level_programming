#!/usr/bin/python3
"""Safe function."""
import sys


def safe_function(fct, *args):
    """Execute a function safely."""
    try:
        return fct(*args)
    except BaseException as err:
        print("Exception:", err, file=sys.stderr)
        return None
