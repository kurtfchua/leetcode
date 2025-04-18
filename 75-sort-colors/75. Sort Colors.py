class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        counts = [0,0,0] # use 0,1,2 as keys when iterating through nums

        for num in nums:
            counts[num] += 1
        
        # reassign elements in numbs while iterating through counts

        i = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1

        return nums

        # T O(n): We iterate through nums 2 separate times. Once to get counts and once to reassign values from counts.
        # S O(1): Counts is defined by our range of numbers that we already knew beforehand, it doesn't grow with the list.
         