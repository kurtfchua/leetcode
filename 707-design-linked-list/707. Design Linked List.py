class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head.next
        for _ in range(index):
            current = current.next
        
        return current.val

        # S O(1): We don't create any new structures
        # T O(n): We iterate through the list until we get to our index
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size +=1
        
        # S O(1): We don't use any new structures relative to input size
        # T O(1): We already know where head is. We instantly access it

    def addAtTail(self, val: int) -> None:
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(val)
        current.next = new_node
        self.size +=1        

        # S O(1): We don't use any new structures relative to input size
        # T O(n): We have to iterate through the entire list to add a new tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self.size +=1
        
        # S O(1): We don't use any new data structures relative to input size
        # T O(n): We must iterate through list until we get to our index

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.size -=1
        
        # S O(1): We don't use any new data structures relative to input size
        # T O(n): We must iterate through list until we get to our index


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)