#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists): A 2-dimensional array of integers.

    Returns:
        list of lists: A new matrix with the same size as the input matrix,
                       where each value is the square of the corresponding
                       value in the input matrix.
    """
    new_matrix = []
    for row in matrix:
        squared_row = list(map(lambda x: x**2, row))
        new_matrix.append(squared_row)
    return new_matrix
