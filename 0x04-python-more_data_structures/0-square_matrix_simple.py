#!/usr/bin/python3
"""Function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square of all values in a matrix."""
    return [map(lambda x: x ** 2, row) for row in matrix]
