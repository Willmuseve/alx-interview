#!/usr/bin/python3

"""
This program Rotates 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """
    The actual fnction that rotates 2-d matrix.
    """
    if matrix is None:
        return

    y = len(matrix)

    # Transpose the matrix
    for i in range(y):
        for j in range(i, y):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
