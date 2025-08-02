class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the counts in nums for each num in a counter hashmap
        # heapify a list with the counts as well as the num 
        counts_map = Counter(nums)
        heap = [(v, k) for k, v in counts_map.items()]
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        for elem in heap:
            res.append(elem[1])

        return res