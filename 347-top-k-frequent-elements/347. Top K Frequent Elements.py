class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for key, value in hashmap.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res


        