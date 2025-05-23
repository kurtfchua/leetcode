class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for num in nums: 
            curr_sum = num + max(curr_sum, 0)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum


        # T O(n) S O(1)
        