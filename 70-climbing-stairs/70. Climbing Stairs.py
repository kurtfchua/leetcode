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

        #return basic(n)
        return top_bottom(n)
        