class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)

        def dfs(i):
            if i in visited: 
                return False
            
            visited.add(i)

            for city, val in enumerate(isConnected[i]): 
                if city not in visited and val == 1: 
                   dfs(city)
            
            return True
        
        provinces = 0
        for i in range(n):
            if i not in visited: 
                if dfs(i):
                    provinces += 1

        return provinces
            