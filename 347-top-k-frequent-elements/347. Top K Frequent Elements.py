class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []

        for n, v in counter.items():
            heapq.heappush(min_heap, (v, n))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res
        