class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = Counter(nums)
        heap = [(count, num) for num, count in counts_map.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [num for count, num in heap]