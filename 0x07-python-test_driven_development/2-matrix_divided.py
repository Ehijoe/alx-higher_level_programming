#!/usr/bin/python3
"""Divide a matrix."""


def divide(a, b):
    """Divide a by b and return the value to 2dp."""
    c = a / b
    if a % b == 0:
        return int(c)
    return round(c, 2)


def matrix_divided(matrix, div):
    """Divide each element in matrix by div."""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )

    # Check if rows have equal sizes
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[divide(num, div) for num in row] for row in matrix]
