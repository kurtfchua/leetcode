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

        # T O(n) - each for loop is iterating through the length of the list. except the last for loop where we touch each element in the list only once. the entire nested for loop is O(n).
        # S O(n) - we create a hashmap, bucket and res lists of size n.


        