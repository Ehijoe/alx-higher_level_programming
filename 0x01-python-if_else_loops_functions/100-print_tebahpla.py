#!/usr/bin/python3
"""Smile in the mirror."""

for i in range(ord('z'), ord('a') - 1, -1):
    num = i if i % 2 == 0 else i - 32
    print("{}".format(chr(num)), end="")
