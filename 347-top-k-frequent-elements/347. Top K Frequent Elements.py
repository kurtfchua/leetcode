class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-v, i) for i, v in freq.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        