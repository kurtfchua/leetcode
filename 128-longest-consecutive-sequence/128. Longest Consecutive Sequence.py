class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for num in hashset: 
            if num - 1 not in hashset:
                next_longest = 1
                while num + next_longest in hashset:
                    next_longest += 1
                longest = max(longest, next_longest)
        
        return longest


        