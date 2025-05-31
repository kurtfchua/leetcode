class Solution:
    def fib(self, n: int) -> int:

        def basic(n):
            if n <= 1: 
                return n 

            return basic(n-2) + basic(n-1)
        
        return basic(n)
        