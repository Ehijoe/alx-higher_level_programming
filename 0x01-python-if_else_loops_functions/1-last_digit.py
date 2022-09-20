#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

if number < 0:
    last_digit = 0 - last_digit

value = "and is less than 6 and not 0"

if last_digit > 5:
    value = "and is greater than 5"
elif last_digit == 0:
    value = "and is zero"

print(f"The last digit of {number} is {last_digit} {value}")
