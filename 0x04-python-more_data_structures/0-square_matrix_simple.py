#!/usr/bin/python3
"""Function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square of all values in a matrix."""
    if matrix is None:
        return []
    if len(matrix) == 0:
        return []
    return [list(map(lambda x: x ** 2, row)) for row in matrix]


if __name__ == '__main__':
    mat = square_matrix_simple([
        [1, 2, 3],
        [4, 5, 6],
    ])
    print(mat)
