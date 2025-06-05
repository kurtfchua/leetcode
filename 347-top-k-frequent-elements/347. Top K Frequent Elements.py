class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = Counter(nums)
        min_heap = []

        for key, v in counts_map.items():
            heapq.heappush(min_heap, (v, key))

            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
        