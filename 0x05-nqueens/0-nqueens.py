#!/usr/bin/python3
"Import system module for N Queens solution to finder module"

import sys


solutions = []  # list of possible solutions
n = 0  # size of the chessboard
positions = None  # listd of possible positions on the chessboard


def get_input():
    """ThIS function gets the size of the chessboard from the command
    line arguments"""
    global n
    n = 0

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Check if two positions are on each other
    """
    if (pos0[0] == pos1[0]) or \
       (pos0[1] == pos1[1]) or \
       (abs(pos0[0] - pos1[0])) == (abs(pos0[1] - pos1[1])):
        return (True)
    return (False)


def group_exists(group):
    """Check if a group of positions already exists in the list of positions
    """
    global solutions

    for x in solutions:
        i = 0
        for y in x:
            for z in group:
                if y[0] == z[0] and y[1] == z[1]:
                    i += 1
        if i == n:
            return (True)
    return (False)


def build_solution(row, group):
    """Build a solution to the n queens problem.
    """
    global solutions
    global n

    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
        return

    for col in range(n):
        a = (row * n) + col
        matches = zip(list([positions[a]]) * len(group), group)
        used_positions = map(
            lambda x: is_attacking(x[0], x[1]), matches)

        if not any(used_positions):
            group.append(positions[a].copy())
            build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Get the solutions for the N Queens problem"""
    global positions, n

    positions = list(map(lambda x: [x // n, x % n], range(n * n)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
