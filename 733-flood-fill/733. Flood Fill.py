class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        def dfs(r, c, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or image[r][c] != original_color: 
                return 
            
            visited.add((r,c))
            image[r][c] = color

            dfs(r-1, c, visited)
            dfs(r+1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        dfs(sr, sc, set())

        return image            

            
        