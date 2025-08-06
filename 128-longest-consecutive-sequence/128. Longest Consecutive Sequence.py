class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in seen:
            length = 1
            if num-1 not in seen:
                while num + length in seen:
                    length += 1

            res = max(res, length)
        
        return res

        