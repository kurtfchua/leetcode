class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)

        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, target, visited): 
            if node in visited: 
                return False
            if node == target: 
                return True
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if dfs(neighbor, target, visited):
                    return True

            return False
        
        return dfs(source, destination, set())