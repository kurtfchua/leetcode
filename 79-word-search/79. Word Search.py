class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (0 > r or r >= rows or
                0 > c or c >= cols or
                board[r][c] == "#" or
                board[r][c] != word[i]):
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            word_exists = (dfs(r+1, c, i+1) or 
                           dfs(r, c+1, i+1) or 
                           dfs(r-1, c, i+1) or
                           dfs(r, c-1, i+1))
            board[r][c] = tmp

            return word_exists
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): 
                        return True
        
        return False