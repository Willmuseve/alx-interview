#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = set()
    visited.add(0)  # Mark the first box as visited
    queue = deque([0])  # Start BFS from the first box
    
    while queue:
        current_box = queue.popleft()
        
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)
    
    return len(visited) == n

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
