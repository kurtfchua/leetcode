class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
       
        def dfs(r,c):
            if r < 0 or r>= rows or c < 0 or c>= cols or grid[r][c] != 1: 
                return 0

            grid[r][c] = 0
            area = 0
            area += 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r,c-1) + dfs(r, c+1)

            return area

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 0
            area = 1
            while queue: 
                r, c = queue.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for dr, dc in directions: 
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == 1:
                        area += 1
                        grid[r+dr][c+dc] = 0
                        queue.append((r+dr, c+dc))
            
            return area 

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    max_area = max(max_area, bfs(r,c))

        return max_area

        