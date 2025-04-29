class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        def memo(r, c, ROWS, COLS, cache):
            if r == ROWS or c == COLS:
                return 0 
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            cache[r][c] = memo(r+1, c, ROWS, COLS, cache) + memo(r, c+1, ROWS, COLS, cache)
            
            return cache[r][c]
        
        def dp(rows,cols):
            prev_row = [0 for _ in range(cols)]

            for _ in range(rows-1, -1, -1):
                current_row = [0 for _ in range(cols)]
                current_row[cols-1] = 1
                for c in range(cols-2, -1, -1):
                    current_row[c] = current_row[c+1] + prev_row[c]
                prev_row = current_row
            
            return prev_row[0]
        
        #return memo(0, 0, m, n, cache)
        return dp(m,n)
        