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
        
        dfs(sr, sc)

        return image


        