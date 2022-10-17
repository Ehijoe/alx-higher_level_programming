#!/usr/bin/python3
"""Lazy matrix multiplication."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy."""
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")
    return [list(row) for row in numpy.matmul(m_a, m_b)]
