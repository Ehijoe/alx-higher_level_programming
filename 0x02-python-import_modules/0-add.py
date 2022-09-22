#!/usr/bin/python3
"""A Program to Add two numbers."""
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    value = f"{a} + {b} = {add(a, b)}"
    print(value, end="\n")
