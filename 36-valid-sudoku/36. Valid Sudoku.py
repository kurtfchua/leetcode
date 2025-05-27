class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        boxes_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue

                if (board[r][c] in rows_set[r] or 
                    board[r][c] in cols_set[c] or 
                    board[r][c] in boxes_set[(r//3, c//3)]):
                    return False

                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                boxes_set[(r//3,c//3)].add(board[r][c])
        
        return True