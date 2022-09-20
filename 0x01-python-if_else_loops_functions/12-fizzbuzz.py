#!/usr/bin/python3
"""Fizzbuzz."""


def fizzbuzz():
    """Fizzbuzz."""
    for num in range(1, 101):
        ans = str(num)
        if num % 15 == 0:
            ans = "FizzBuzz"
        elif num % 3 == 0:
            ans = "Fizz"
        elif num % 5 == 0:
            ans = "Buzz"
        print(ans, end=" ")
