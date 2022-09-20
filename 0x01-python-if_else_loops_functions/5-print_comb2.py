#!/usr/bin/python3
"""Print out the alphabet."""

for i in range(99):
    print("{}{}, ".format(i // 10, i % 10), end="")
print("99")
