#!/usr/bin/python3
"""Pascal's triangle."""


def pascal_triangle(n):
    """Return a list representing n rows of Pascal's triangle."""
    if type(n) is not int:
        raise TypeError
    if n <= 0:
        return []
    result = [[1]]
    for i in range(n - 1):
        new = [1]
        for j in range(i):
            new.append(result[-1][j] + result[i][j + 1])
        new.append(1)
        result.append(new)
    return result


if __name__ == '__main__':
    for i in range(5):
        print(f"Size {i + 1}")
        for row in pascal_triangle(i + 1):
            print(row)
        print()
