class UnionFind: 
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}

        for i in range(n):
            self.parents[i] = i 
            self.ranks[i] = 0 
    
    def find(self, n): 
        p = self.parents[n]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
    
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: 
            return False
        
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges: 
            if uf.union(u,v):
                n-= 1
        
        return n
        