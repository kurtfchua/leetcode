class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        def memoization(r, c, ROWS, COLS, cache):
            if r == ROWS or c == COLS:
                return 0 
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            if r+1 < ROWS:
                if obstacleGrid[r+1][c] == 0:
                    count += memoization(r+1, c, ROWS, COLS, cache)
            if c+1 < COLS:
                if obstacleGrid[r][c+1] == 0:
                    count += memoization(r,c+1, ROWS, COLS, cache)
            cache[r][c] = count
            
            return cache[r][c]
        
        def dp(rows, cols):
            prev_row = [0 for _ in range(cols)]

            for r in range(rows-1, -1, -1):
                current_row = [0 for _ in range(cols)] 
        
                for c in range(cols-1, -1, -1):
                    if r == rows - 1 and c == cols - 1:
                        current_row[c] = 1
                    elif obstacleGrid[r][c] == 1:
                        current_row[c] = 0
                    else:
                        right_dir = current_row[c+1] if c + 1 < cols else 0
                        down_dir = prev_row[c]
                        current_row[c] = right_dir + down_dir
                        
                prev_row = current_row

            return prev_row[0]
        
        #cache = [[0]*n for _ in range(m)]
        #return memoization(0,0,m,n,cache)

        return dp(m,n)