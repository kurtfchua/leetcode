class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] in seen:
                            return False
                        if board[row + i][col + j] !=".":
                            seen.add(board[row + i][col + j])

        return self.check_row(board,9,9) and self.check_col(board,9,9)
        
        
    def check_row(self, board, m, n):
            for i in range(m):
                row_set = set()
                for j in range(n):
                    if board[i][j] in row_set:
                        return False
                    if board[i][j] != ".":
                        row_set.add(board[i][j])
            return True
        
    def check_col(self, board,m,n):
            for j in range(n):
                col_set = set()
                for i in range(m):
                    if board[i][j] in col_set:
                        return False
                    if board[i][j] != ".":
                        col_set.add(board[i][j])  
            return True



            



