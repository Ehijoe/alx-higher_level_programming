#!/usr/bin/python3
"""Matrix multiplication."""


def check_matrix_types(mat, name):
    """Check if a list of lists is a matrix."""
    for row in mat:
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(
                    f"{name} should contain only integers or floats"
                )


def check_matrix_dimensions(mat, name):
    """Check if the dimensions of a matrix are reasonable."""
    size = len(mat[0])
    for row in mat:
        if len(row) != size:
            raise TypeError(f"each row of {name} must be of the same size")


def transpose(mat):
    """Transpose a matrix.

    Example:
    >>> transpose([[1]])
    [[1]]

    >>> transpose([[1], [1]])
    [[1, 1]]
    """
    row_len = len(mat[0])
    return [[row[i] for row in mat] for i in range(row_len)]


def dot_product(a, b):
    """Find the dot product of two vectors."""
    return sum([a[i] * b[i] for i in range(len(a))])


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    check_matrix_types(m_a, "m_a")
    check_matrix_types(m_b, "m_b")
    check_matrix_dimensions(m_a, "m_a")
    check_matrix_dimensions(m_b, "m_b")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    ans = [[dot_product(row, col) for col in transpose(m_b)] for row in m_a]

    return ans
