class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in seen:
            length = 1
            seq = num 
            if seq-1 not in seen:
                while seq + 1 in seen:
                    length += 1
                    seq += 1
            res = max(res, length)
        
        return res

        