"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        copy = {}
        queue = deque([node])
        copy[node] = Node(node.val)

        while queue: 
            for i in range(len(queue)):
                n = queue.popleft()
                for neighbor in n.neighbors: 
                    if neighbor not in copy:
                        copy[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    copy[n].neighbors.append(copy[neighbor])
                
        return copy[node]