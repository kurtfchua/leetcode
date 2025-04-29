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
        
        cache = [[0]*n for _ in range(m)]

        return memoization(0,0,m,n,cache)