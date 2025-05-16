#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) that is used to divide
             the matrix elements.

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
