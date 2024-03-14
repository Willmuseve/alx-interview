#!/usr/bin/python3

"""
A function that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    This function checks if all the locked boxed can be opened
    """
    x = len(boxes)


    unlocked = [False] * x
    unlocked[0] = True  


    keys_found = [0]


    visited = set()
    visited.add(0)

    while keys_found:
        current_key = keys_found.pop()


        for key in boxes[current_key]:
            if key not in visited:
                visited.add(key)
                unlocked[key] = True
                keys_found.append(key)


    return all(unlocked)
