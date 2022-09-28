#!/usr/bin/python3
"""Roman Numeral converter."""


def roman_to_int(roman_string):
    """Convert a roman numeral to an integer."""
    if type(roman_string) is not str:
        return 0
    roman_vals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    max_val = 0
    number = 0
    for digit in roman_string[::-1]:
        if digit not in roman_vals:
            return 0
        if roman_vals[digit] < max_val:
            number -= roman_vals[digit]
        else:
            number += roman_vals[digit]
            max_val = roman_vals[digit]
    return number


if __name__ == '__main__':
    print(roman_to_int(None))  # 0
    print(roman_to_int(32))  # 0
    print(roman_to_int("asdfghasa"))  # 0
    print(roman_to_int("X"))  # 10
    print(roman_to_int("XIII"))  # 13
    print(roman_to_int("XIV"))  # 14
    print(roman_to_int("DCCXC"))  # 790
    print(roman_to_int("IX"))  # 9
