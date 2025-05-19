# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head 

        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth_node = self.get_kth(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next
            prev, current = kth_node.next, group_prev.next
            while current != group_next:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            tmp = group_prev.next
            group_prev.next = kth_node
            group_prev = tmp
        return dummy.next
            
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr