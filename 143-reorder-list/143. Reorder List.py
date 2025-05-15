# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        
        current = head
        for _ in range(len(stack)//2):
            tmp = current.next
            node = stack.pop()
            current.next = node
            node.next = tmp 
            current = tmp
        current.next = None
            
        