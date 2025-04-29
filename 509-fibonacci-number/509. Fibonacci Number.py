class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n
        
        dp = [0,1]
        i = 2
        while i <= n:
            dp[0], dp[1] = dp[1], dp[1] + dp[0]
            i += 1
        
        return dp[1]
        