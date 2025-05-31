class Solution:
    def rob(self, nums: List[int]) -> int:
        
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
        #return max(dp_top(0, skip_first, mem1), dp_top(0, skip_end, mem2))

        def dp_bottom(nums):
            rob1, rob2 = 0, 0

            for num in nums: 
                temp = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(nums[0], dp_bottom(skip_first), dp_bottom(skip_end))