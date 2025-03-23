# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """     
        With each node we visit we must set the next value to whatever prev value we had
        To get a prev value we update it with each Node starting from None to whatever we had
        recently.

        We keep a next node value before we change the next value so we can traverse to the 
        next node in the list. We also update the prev value before we advance to this next 
        value to use in the next iteration

        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

        # Space Complexity: We do this in-place without using any new data structure, O(1)
        # Time Complexity: We must traverse through the entire linked list to reverse pointers, O(n)