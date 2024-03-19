#!/usr/bin/python3

"""
A program that returns a list of integers representing the pascal's
trianfle of n
"""


def pascal_triangle(n):
    """
    The function that creates pascals triangle.
    """
    ans = []

    if n <= 0:
        return {}

    for _ in range(n):
        row = [1]
        if ans:
            row_x = ans[-1]
            row.extend([sum(pair) for pair in zip(row_x, row_x[1:])])
            row.append(1)
        ans.append(row)

    return ans
