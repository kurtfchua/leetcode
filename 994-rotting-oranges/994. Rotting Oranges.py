class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
        
        minutes = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions: 
                    if (0<= r+dr < rows and 0 <= c+dc <cols and 
                        (r+dr, c+dc) not in visited and 
                        grid[r+dr][c+dc] == 1):
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
            minutes += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if minutes > 0 else 0