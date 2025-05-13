class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        i = 0 
        while i < len(nums):
            if nums[i] > 0:
                min_val = nums[i]
                for j in range(len(nums)):
                    nums[j] -= min_val
                count += 1
            else:
                i +=1
        return count        