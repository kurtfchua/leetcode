class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        visited = set()

        def dfs(i):
            if i in visited: 
                return 
            
            visited.add(i)

            for idx, val in enumerate(isConnected[i]):
                if val == 1: 
                    if idx not in visited: 
                        dfs(idx)
        
        count = 0
        for r in range(rows): 
                if r not in visited: 
                    dfs(r)
                    count += 1
        
        return count 
        