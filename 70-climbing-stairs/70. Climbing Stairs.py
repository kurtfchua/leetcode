class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            # base case: when we try to get to step 1 or 2
            # 1 unique way to get to step 1, and 2 unique ways to get to step 2
            if n == 1 or n == 2: return n 
            # if result exists in memory just return result
            if n in memo: return memo[n]
            # counting all paths that start at step 0 and reach step n
            # either taking 1 or 2 steps from a current step
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        #return dfs(n)

        def dp(n):
            if n <= 2:
                return n
            dp = [1,2]
            i = 3

            while i <= n:
                dp[0], dp[1] = dp[1], dp[1] + dp[0]
                i += 1
            return dp[1]
        return dp(n)
        
        # T O(n): we memo each result after exploring the longest branch. each subproblem is solved once
        # S O(n): n is the maximum depth of the tree we travel when collapsing the call stack