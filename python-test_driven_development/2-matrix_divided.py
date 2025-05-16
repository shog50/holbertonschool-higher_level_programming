#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding results to 2 decimals.

    Args:
        matrix: list of lists of integers/floats
        div: number to divide each element by

    Returns:
        A new matrix with divided values

    Raises:
        TypeError: if matrix is not list of lists of numbers, or div not number
        ZeroDivisionError: if div is zero
    """
    if matrix is None or div is None:
        raise TypeError("missing required argument")

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        # return matrix of zeros same size as input
        return [[0.0 for _ in row] for row in matrix]

    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
