class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        starting_color = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or image[r][c] != starting_color: 
                return 
            
            image[r][c] = color
            visited.add((r,c))

            dfs(r-1, c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        
        def bfs(r, c):
            queue = deque([(r,c)])
            visited = set([(r,c)])      
            image[r][c] = color

            while queue: 
                r, c = queue.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for dr, dc in directions: 
                    if (0 <= r + dr < rows and 0 <= c + dc < cols 
                    and (r+dr, c+dc) not in visited and image[r+dr][c+dc] == starting_color): 
                        image[r+dr][c+dc] = color
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
        
        #dfs(sr, sc)
        bfs(sr, sc)
        
        return image


        