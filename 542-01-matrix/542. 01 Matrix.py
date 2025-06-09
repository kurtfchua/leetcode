class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0: 
                    queue.append((r,c))
                    visited.add((r,c))
    
        
        level = 1
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions: 
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and (r+dr, c+dc) not in visited and mat[r+dr][c+dc] == 1:
                        mat[r+dr][c+dc] = level
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            level+=1

        return mat 
        
    