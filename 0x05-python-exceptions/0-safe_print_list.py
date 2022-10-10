#!/usr/bin/python3
"""Safe list printing."""


def safe_print_list(my_list=[], x=0):
    """Print the item at a particular index of a list."""
    printed = 0
    try:
        for i in range(x):
            printed += 1
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
        return printed
