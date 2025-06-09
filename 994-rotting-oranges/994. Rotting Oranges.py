class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: 
                    queue.append((r,c))
                    visited.add((r,c))

        minutes = -1
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(0,-1),(-1,0)]
                for dr, dc in directions: 
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == 1: 
                        grid[r+dr][c+dc] = 2
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            minutes += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    return -1
        
        return minutes if minutes > 0 else 0 