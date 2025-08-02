class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = Counter(nums)
        heap = []

        for num, count in counts_map.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
        