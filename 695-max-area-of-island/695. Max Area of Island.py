class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = 0
            area = 1

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    directions = [(0,1),(1,0),(0,-1),(-1,0)]
                    for dr, dc in directions:
                        if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == 1:
                            queue.append((r+dr,c+dc))
                            area += 1
                            grid[r+dr][c+dc] = 0
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))

        return max_area
        