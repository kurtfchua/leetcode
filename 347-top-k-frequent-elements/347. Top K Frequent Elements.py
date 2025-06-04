class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        min_heap = []

        for key, val in nums_count.items(): 
            heapq.heappush(min_heap, (val, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res 
        