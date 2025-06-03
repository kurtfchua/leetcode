class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0 
            
            LIS = dfs(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1+dfs(i+1, i))
            
            return LIS
        
        #return dfs(0, -1)

        mem = {}
        def top_down(i, j):
            if i == len(nums):
                return 0 
            if (i, j)in mem: 
                return mem[(i,j)]

            LIS = top_down(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1+top_down(i+1, i))
            
            mem[(i,j)] = LIS

            return LIS
        
        #return top_down(0, -1)
        
        def bottom_up():
            dp = [1] * len(nums)

            for i in range(len(nums)-1,-1,-1):
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], 1+dp[j])
            
            return max(dp)
        
        return bottom_up()