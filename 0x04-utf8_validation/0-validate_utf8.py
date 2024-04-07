#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Function returns True if data is a valid UTF-8 encoding otherwise False
    """
    y = 0
    n = len(data)

    for i in range(n):
        if y > 0:
            y -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return (False)
        elif data[i] <= 0x7f:
            y = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return (False)
                y = span - 1
            else:
                return (False)
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return (False)
                y = span - 1
            else:
                return (False)
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return (False)
                y = span - 1
            else:
                return (False)
        else:
            return (False)
    return (True)
