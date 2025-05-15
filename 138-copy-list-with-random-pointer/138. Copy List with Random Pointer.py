"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head
        
        hashmap = {}
        current = head
        while current:
            hashmap[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            new_node = hashmap[current] if current else None
            new_node.next = hashmap[current.next] if current.next else None
            new_node.random = hashmap[current.random] if current.random else None
            current = current.next

        return hashmap[head]
        