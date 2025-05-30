class Solution:
    def climbStairs(self, n: int) -> int:

        def basic(n):
            if n <= 2: 
                return n
            
            return basic(n-1) + basic(n-2)
        
        mem = {}
        def top_down(n):
            if n <= 2: 
                return n 
            
            if n in mem: 
                return mem[n]
                
            mem[n] = top_down(n-1) + top_down(n-2)

            return mem[n]

        return top_down(n)
        #return basic(n)
        