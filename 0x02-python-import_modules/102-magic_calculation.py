#!/usr/bin/python3
"""Don't stop the magic."""
import dis


def magic_calculation(a, b):
    """Do some magic.

    Who knows what it does?
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c

    return sub(a, b)


if __name__ == '__main__':
    dis.dis(magic_calculation)
