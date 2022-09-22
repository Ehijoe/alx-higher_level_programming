#!/usr/bin/python3
"""Display hidden names."""

import hidden_4

if __name__ == '__main__':
    names = [name for name in dir(hidden_4) if name[:2] != "__"]
    names.sort()
    for name in names:
        print(name)
