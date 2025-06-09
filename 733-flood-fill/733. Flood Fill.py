class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        original_color = image[sr][sc]
        def dfs(r, c): 
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color or (r,c) in visited:
                return 

            visited.add((r,c))
            image[r][c] = color

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r,c-1)
            dfs(r,c+1)

        def bfs(r,c):
            queue = deque([(r,c)])
            visited = set([r,c])
            image[r][c] = color

            while queue: 
                r, c = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions: 
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and image[r+dr][c+dc] == original_color and (r+dr,c+dc) not in visited: 
                        image[r+dr][c+dc] = color
                        visited.add((r+dr,c+dc))
                        queue.append((r+dr,c+dc))

        #dfs(sr,sc)
        bfs(sr,sc)

        return image 
        