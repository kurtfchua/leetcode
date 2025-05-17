class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def insert_at_end(self, node):
        mru_node = self.right.prev
        mru_node.next = self.right.prev = node
        node.prev, node.next = mru_node, self.right

    def get(self, key: int) -> int:
        if not key in self.cache: return -1
        self.remove(self.cache[key])
        self.insert_at_end(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert_at_end(self.cache[key])
        else:
            node = Node(key, value)
            self.insert_at_end(node)
            self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)