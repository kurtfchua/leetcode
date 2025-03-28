# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Create a dummy node to attach to head.
        Create a prev pointer to dummy.

        Iterating through the list we check if node.val == val.
        If node.val == val, we set the prev.next to current.next
        else we update prev pointer to the current pointer
        we then update the current pointer to the next node

        Return dummy.next
        """
        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next

        # S O(1) We don't create any new DSA relative to the input size
        # T O(n) We must iterate through the entire list to see all instances of the value