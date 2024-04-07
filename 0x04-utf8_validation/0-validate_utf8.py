#!/usr/bin/python3

"""
A method that determines if a given
data set represents a valid UTF-8 encoding
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    A function that takes a List of integers and returns True if they
    represent a valid UTF-8 encoding and False otherwise.
    """
    data = iter(data)
    for lam in data:
        o = count_leading_ones(lam)
        if o in [1, 7, 8]:
            return False  # Illegal leading byte
        for _ in range(o - 1):
            t = next(data, None)
            if t is None or t >> 6 != 0b10:
                return False  # Missing or illegal trailing byte
    return True


def count_leading_ones(byte):
    """
    Count the number of leading ones in a byte.
    """
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8
