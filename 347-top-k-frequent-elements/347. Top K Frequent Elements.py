class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts for nums
        # get sorted values list for the hashmap
        # append to output array the keys whose values match the sorted values
        # return immediately if len of res is == k 
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        sorted_vals = sorted(list(set(hashmap.values())), reverse=True)
        res =[]
        for v in sorted_vals:
            for num in hashmap:
                if len(res) == k:
                    return res
                if hashmap[num] == v:
                    res.append(num)
        
        return res