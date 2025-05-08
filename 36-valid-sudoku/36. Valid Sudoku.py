class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows if unique elements
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set:
                    return False
                if board[i][j] != ".":
                    row_set.add(board[i][j])
        
        # check all cols if unique elements
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] in col_set:
                    return False
                if board[i][j] != ".":
                    col_set.add(board[i][j])
        
        # check each 3x3 box, iterate 3x3 box and see if all unique
        for i in range(0,9,3):
            for j in range(0,9,3):
                box_set = set()
                for row in range(3):
                    for col in range(3):
                        if board[i+row][j+col] in box_set:
                            return False
                        if board[i+row][j+col] != ".":
                            box_set.add(board[i+row][j+col])
        
        return True