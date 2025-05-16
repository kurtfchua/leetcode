class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
    
    def add(self, node):
        node_prev = self.right.prev
        node_prev.next = node
        self.right.prev = node
        node.prev = node_prev
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        if node.next == self.right and self.right.prev == node:
            return node.val

        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cache[node.key] = node
        
        self.add(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            if lru == self.right:
                return
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)