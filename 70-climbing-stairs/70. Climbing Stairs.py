class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n <= 2: return n 

            if n in memo: return memo[n]

            memo[n] = dfs(n-1) + dfs(n-2)

            return memo[n]
       
        def dp(n):
            if n <= 2:
                return n
            dp = [1,2]
            i = 3

            while i <= n:
                dp[0], dp[1] = dp[1], dp[1] + dp[0]
                i += 1
            return dp[1]
        return dfs(n)
        #return dp(n)
        
        # T O(n): we memo each result after exploring the longest branch. each subproblem is solved once
        # S O(n): n is the maximum depth of the tree we travel when collapsing the call stack