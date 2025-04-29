class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        def dfs(r, c, ROWS, COLS, cache):
            if r == ROWS or c == COLS:
                return 0 
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            cache[r][c] = dfs(r+1, c, ROWS, COLS, cache) + dfs(r, c+1, ROWS, COLS, cache)
            
            return cache[r][c]

        return dfs(0, 0, m, n, cache)
        