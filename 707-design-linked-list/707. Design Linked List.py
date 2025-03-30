class Node:
    # Double pointer node
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    # Doubly Linked List
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        # Start iterating from dummy head node until index
        # return value of the current node
        
        # if index is out of range return -1
        if index >= self.size: return -1

        # Start at actual first none dummy node
        current = self.head.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        # create new node with new value
        # new node will be pointed to dummy.next
        # dummy.next.prev will point to new node
        # dummy.next will point to new node
        # increment size

        new_node = Node(val)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1   

    def addAtTail(self, val: int) -> None:
        # create new node with val
        # get dummy.prev to point next to new node
        # get new node to point prev to dummy.prev and next to dummy
        # get dummy to point prev to new node 
        # increment size
        new_node = Node(val)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        # iterate through list until we get to before the index
        # create new node with val
        # assign current.next prev pointer to new node
        # assign new_node.next to current.next
        # assign new_node.prev to current
        # assign current.next to new node
        # increment size

        # if index > size don't insert
        if index > self.size: return 

        current = self.head
        for _ in range(index):
            current = current.next
        new_node = Node(val)
        current.next.prev = new_node
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        # iterate through list from dummy node until before the index
        # assign current.next to current.next.next
        # assign current.next.next prev pointer to current
        # decrement size

        # if index >= size we don't delete anything
        if index >= self.size: return 

        current = self.head 
        for _ in range(index):
            current = current.next

        elim_node = current.next
        current.next = elim_node.next
        elim_node.next.prev = current
        self.size -= 1        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)