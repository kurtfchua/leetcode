class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n <=1: return n

        # call fib on both n-1 and n-2 and get sum
        return self.fib(n-1) + self.fib(n-2)

        # T O(2^n): we add a new level of 2 new nodes to the recursion tree with each call
        # S O(n): n is the maximum depth of the tree we travel when collapsing the call stack
        