class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.push(num)
            if len(self.heap) > self.k:
                self.pop()
        
    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) > self.k:
            self.pop()
        
        return self.heap[0]

    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        
        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2

    def pop(self):
        if not self.heap:
            return self.heap
        if len(self.heap) == 1:
            return self.heap.pop()

        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0

        while 2*i+1 < len(self.heap):
            # check if right child exists
            # check if right < left
            # check if right < new node
            if ((2*i+2) < len(self.heap) and
            self.heap[2*i+2] < self.heap[2*i+1] and
            self.heap[2*i+2] < self.heap[i]):
                self.heap[2*i+2], self.heap[i] = self.heap[i], self.heap[2*i+2]
                i = 2*i+2
            elif self.heap[2*i+1] < self.heap[i]:
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2*i+1
            else:
                break

        return res


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)