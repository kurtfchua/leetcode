class MedianFinder:

    def __init__(self):
        self.stream = []
        
    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        self.stream.sort()
        size = len(self.stream)
        if len(self.stream) % 2 == 0: 
            return (self.stream[size//2] + self.stream[(size//2)-1]) / 2
        else: 
            return self.stream[size//2]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()