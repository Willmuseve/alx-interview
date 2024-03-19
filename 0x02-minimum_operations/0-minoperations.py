#!/usr/bin/python3
"""
This program finds the minimum operations needed to perform a task.
"""


def minOperations(n: int) -> int:
    """
    This function calculates fewest no of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    def new_func(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    numbs = new_func(n)

    if not numbs:
        return 0

    ops = 0
    for i in numbs:
        ops += i

    return ops
