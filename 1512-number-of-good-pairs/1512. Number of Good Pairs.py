class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # we get frequency of each num in nums as we iterate
        # with each element found can create pairs with all equal elements before it
        # we add its frequency to counts
        nums_freq = {}
        counts = 0 

        for num in nums: 
            counts += nums_freq.get(num, 0)
            nums_freq[num] = nums_freq.get(num, 0) + 1
        
        return counts

        # T O(n): we must iterate through all of nums to get frequencies of nums
        # S O(n): we create dictionary that grows relative to nums