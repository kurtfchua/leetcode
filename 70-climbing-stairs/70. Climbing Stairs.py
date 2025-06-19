class Solution:
    def climbStairs(self, n: int) -> int:

        def recur(n): 
            if n <= 2: 
                return n 
            
            return recur(n-1) + recur(n-2)
        
        mem = {}
        def top_down(n):
            if n in mem: 
                return mem[n]
            if n <= 2: 
                return n 
            
            mem[n] = top_down(n-1) + top_down(n-2)
            return mem[n]

        #return recur(n)
        return top_down(n)