# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Make an initial null dummy node that we will attach to once we start iterating through l1 and l2.
        We then iterate through both l1 and l2, comparing values. Current.next will be assigned to whichever value in both lists is smaller. We then assign the next value to be compared from whicever we choose.
        In the case that either list is exhausted first, we attach the rest of the other list to the new list
        The head of this new list will be refernced by dummy.next
        Return dummy.next
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next

        # S O(m+n) we create a new linked list with the length of the sum of both lists
        # T O(m+n) we have to go through both lists to create the new list