class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []

        for num, count in freq.items() : 
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res


        