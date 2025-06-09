class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        for r in range(rows): 
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        level = 1
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions: 
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and rooms[r+dr][c+dc] != -1 and (r+dr,c+dc) not in visited: 
                        rooms[r+dr][c+dc] = level
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            level += 1
        
        return
