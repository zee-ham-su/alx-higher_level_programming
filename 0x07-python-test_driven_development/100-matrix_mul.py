#!/usr/bin/python3
"""
Multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If either m_a or m_b is not a list or not a list
        of lists.
        ValueError: If either m_a or m_b is empty, or if the
        matrices cannot be multiplied.
        TypeError: If m_a or m_b contains elements that are not
        integers or floats.
        TypeError: If the rows of m_a are not all the same size or
        the rows of m_b are not all the same size.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError('m_a must be a list or m_b must be a list')
    if not all(isinstance(row, list) for row in m_a) or \
       not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_a must be a list of lists or m_b '
              'must be a list of lists')
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for
               num in row) or \
       not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError('m_a should contain only integers or floats or '
                        'm_b should contain only integers or floats')
    if not all(len(row) == len(m_a[0]) for row in m_a) or \
       not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_a must be of the same size or '
                        'each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)]
            for row_a in m_a]
