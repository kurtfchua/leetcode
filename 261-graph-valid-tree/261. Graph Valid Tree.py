class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: 
            return True
        
        adj_list = {i:[] for i in range(n)}

        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
    
        def dfs(node, parent):
            if node in visited: 
                return False
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
        
        