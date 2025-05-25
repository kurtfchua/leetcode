class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word): return True
            if (r < 0 or r >= rows or
               c < 0 or c >= cols or 
               board[r][c] != word[i] or
               board[r][c] == "#"):
                    return False
    
            board[r][c] = "#"
            found_word = (
                dfs(r+1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c-1, i+1)
                )
            board[r][c] = word[i]

            return found_word
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]: 
                    if dfs(r,c,0):
                        return True

        return False        