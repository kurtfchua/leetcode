class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] == "#" or
                board[r][c] != word[i]):
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            up = dfs(r-1, c, i+1)
            down = dfs(r+1, c, i+1)
            left = dfs(r, c-1, i+1)
            right = dfs(r, c+1, i+1)

            board[r][c] = tmp
            
            return up or down or left or right
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False