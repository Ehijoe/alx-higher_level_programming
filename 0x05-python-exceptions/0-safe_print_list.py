#!/usr/bin/python3
"""Safe list printing."""


def safe_print_list(my_list=[], x=0):
    """Print the item at a particular index of a list."""
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except BaseException:
        pass
    finally:
        print()
        return printed
