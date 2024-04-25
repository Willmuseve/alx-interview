#!/usr/bin/python3

"""
This program Rotates 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """
    The actual fnction that rotates 2-d matrix.
    """
    if x is None:
        return

    y = len(x)

    # Transpose the matrix
    for i in range(y):
        for j in range(i, y):
            x[i][j], x[j][i] = x[j][i], x[i][j]

    # Reverse each row
    for row in x:
        row.reverse()
