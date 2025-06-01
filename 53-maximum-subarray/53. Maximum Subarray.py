class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]

        for num in nums: 
            cur_sum  = num + max(cur_sum, 0)
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
        