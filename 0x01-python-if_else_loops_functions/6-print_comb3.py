#!/usr/bin/python3
"""Print combinations of two digit numbers."""

for i in range(10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end="")
        if i * 10 + j == 89:
            print()
        else:
            print(", ", end="")
