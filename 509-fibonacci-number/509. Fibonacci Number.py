class Solution:
    def fib(self, n: int) -> int:

        def basic(n):
            if n <= 1: 
                return n 

            return basic(n-2) + basic(n-1)
        
        mem = {}
        def top_down(n):
            if n <= 1: 
                return n
            if n in mem: 
                return mem[n]
            
            mem[n] = top_down(n-2) + top_down(n-1)

            return mem[n]


        #return basic(n)
        return top_down(n)


        