class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        def dfs(i, nums):
            if i >= len(nums):
                return 0 

            return max(nums[i] + dfs(i+2, nums), dfs(i+1, nums))
        
        skip_first, skip_end = nums[1:], nums[:-1]
        #return max(dfs(0, skip_first), dfs(0, skip_end))

        def dp_top(i, nums, mem):
            if i >= len(nums):
                return 0
            if i in mem: 
                return mem[i]
            
            mem[i] = max(nums[i]+dp_top(i+2, nums, mem), dp_top(i+1, nums, mem))

            return mem[i]

        mem1, mem2 = {}, {}
        return max(dp_top(0, skip_first, mem1), dp_top(0, skip_end, mem2))