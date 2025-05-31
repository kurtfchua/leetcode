class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i): 
            if i >= len(nums):
                return 0 
            
            return max(nums[i] + dfs(i+2), dfs(i+1))
        
        #return dfs(0)
        mem = {}
        def dp_top(i):
            if i >= len(nums):
                return 0 
            if i in mem: 
                return mem[i]

            mem[i] = max(nums[i] + dp_top(i+2), dp_top(i+1))

            return mem[i]
        
        return dp_top(0)