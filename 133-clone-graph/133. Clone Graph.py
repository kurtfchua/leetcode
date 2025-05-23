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
        
        hashmap = {}

        def bfs(source):
            queue = deque([source])
            hashmap[source] = Node(source.val)

            while queue: 
                for i in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in node.neighbors:
                        if neighbor not in hashmap:
                            hashmap[neighbor] = Node(neighbor.val)
                            queue.append(neighbor)
                        hashmap[node].neighbors.append(hashmap[neighbor])
            return hashmap[source]

        return bfs(node)
        