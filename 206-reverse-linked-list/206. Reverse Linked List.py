# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        We can solve recursively by calling the function on the next node as the new head
        When it reaches the base case where head.next is None or head is None 
        We assign the new head next value to be the current head in the call. 
        We then set the head.next to None to break the pointer.

        Return new head as the newly reversed linked list
        """
        """
        # recursive method

        # base case
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead

        # S O(n) We recursively call all the values in the linked list in the call stack: O(n)
        # T O(n) We traverse through the entire linkedlist to reverse the pointers
        """
        """     
        With each node we visit we must set the next value to whatever prev value we had
        To get a prev value we update it with each Node starting from None to whatever we had
        recently.

        We keep a next node value before we change the next value so we can traverse to the 
        next node in the list. We also update the prev value before we advance to this next 
        value to use in the next iteration

        """

        # iterative method
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
        # Space Complexity: We do this in-place without using any new data structure, O(1)
        # Time Complexity: We must traverse through the entire linked list to reverse pointers, O
