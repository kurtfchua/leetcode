class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = set(nums)
        res = 0

        for num in sequences: 
            if num-1 not in sequences: 
                length = 1
                seq = num
                while seq + 1 in sequences: 
                    length += 1
                    seq = seq + 1
                res = max(res, length)
        
        return res
        