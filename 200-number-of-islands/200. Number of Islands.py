class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r,c)])
            grid[r][c] == "0"

            while queue: 
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    directions = [(0,1),(1,0),(0,-1),(-1,0)]
                    for dr, dc in directions: 
                        if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == "1":
                            queue.append((r+dr, c+dc))
                            grid[r+dr][c+dc] = "0" 
       
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    num_islands += 1

        return num_islands       
