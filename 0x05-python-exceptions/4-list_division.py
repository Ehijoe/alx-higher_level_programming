#!/usr/bin/python3
"""List Division."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide each element in my_list_1 by the corresponding element."""
    result = [0] * list_length
    try:
        for i in range(list_length):
            val = 0
            try:
                val = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            finally:
                result[i] = val
    except IndexError:
        print("out of range")
    finally:
        return result
