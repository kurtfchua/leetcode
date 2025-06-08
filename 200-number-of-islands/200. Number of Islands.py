class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c): 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"        
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        def bfs(r,c):
            queue = deque([(r,c)])

            while queue: 
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions:
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == "1":
                        grid[r+dr][c+dc] = "0"
                        queue.append((r+dr, c+dc))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    #dfs(r,c)
                    bfs(r,c)
                    count += 1
        
        return count