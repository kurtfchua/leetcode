class Solution:
    def climbStairs(self, n: int) -> int:

        def basic(n):
            if n <= 2: 
                return n 
            
            return basic(n-1) + basic(n-2)
        
        mem = {}
        def top_bottom(n):
            if n <= 2:
                return n
            if n in mem:
                return mem[n]
            
            mem[n] = top_bottom(n-1) + top_bottom(n-2)

            return mem[n]
        
        def bottom_up(n):
            if n <= 2:
                return n 
            
            a, b = 1, 2
            i = 3
            while i <= n:
                a, b = b, a+b
                i += 1

            return b 

        #return basic(n)
        #return top_bottom(n)
        return bottom_up(n)
        