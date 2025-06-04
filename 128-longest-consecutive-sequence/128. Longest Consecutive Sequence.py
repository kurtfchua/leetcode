class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            length = 1
            if num-1 not in nums_set:
                seq = num 
                while seq + 1 in nums_set: 
                    length += 1
                    seq = seq + 1
            res = max(res, length)
        
        return res