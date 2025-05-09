# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res1 = []
        res2 = []

        current = head
        while current:
            res1.append(current.val)
            current=current.next

        reverse = self.reverse(head)
        current = reverse
        while current:
            res2.append(current.val)
            current=current.next   

        return res1==res2

    def reverse(self,head):
        if not head: 
            return head
            
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev 
        