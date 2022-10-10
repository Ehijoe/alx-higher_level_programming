#!/usr/bin/python3
"""Magic calculation."""


def magic_calculation(a, b):
    """Do something mystical."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except:
            result = b + a
            break
    return result


if __name__ == '__main__':
    import dis
    dis.dis(magic_calculation)
