#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers using str.format()"""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
