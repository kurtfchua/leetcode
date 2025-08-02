class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the counts in nums for each num in a counter hashmap
        # heapify a list with the counts as well as the num 
        counts_map = Counter(nums)
        heap = []

        for num, v in counts_map.items():
            heapq.heappush(heap, (v, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for v, num in heap:
            res.append(num)

        return res