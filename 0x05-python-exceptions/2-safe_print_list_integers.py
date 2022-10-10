#!/usr/bin/python3
"""Print and count integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in my_list."""
    printed = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except (ValueError, TypeError):
                continue
            printed += 1
    except IndexError:
        pass
    print()
    return printed
