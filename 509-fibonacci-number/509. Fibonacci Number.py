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

        def bottom_up(n):
            if n <= 1: 
                return n 
            
            a, b = 0, 1
            i = 2

            while i <= n: 
                a, b = b, a+b
                i += 1
            
            return b


        #return basic(n)
        #return top_down(n)
        return bottom_up(n)


        