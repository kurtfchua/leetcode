class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        min_heap = [(v,k) for k, v in num_counts.items()]
        heapq.heapify(min_heap)
        
        while len(min_heap) > k: 
            heapq.heappop(min_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res