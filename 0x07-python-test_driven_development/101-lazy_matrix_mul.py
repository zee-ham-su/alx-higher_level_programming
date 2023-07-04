#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        np.ndarray: Resulting matrix after multiplication.
    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("Cannot multiply m_a and m_b") from e
