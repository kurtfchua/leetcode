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

        clones = {}

        def bfs(node):
            queue = deque([node])
            visited = set([node])
            clones[node] = Node(node.val)
            
            while queue: 
                n = queue.popleft()
                for neighbor in n.neighbors: 
                    if neighbor not in clones: 
                        clones[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    clones[n].neighbors.append(clones[neighbor])
        bfs(node)

        return clones[node]
                    
    
        