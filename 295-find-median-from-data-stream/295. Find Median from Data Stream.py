class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        
    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 != 0:
            return -self.left[0]
        else: 
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()