class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        boxes_set = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows_set[i] or
                    board[i][j] in cols_set[j] or
                    board[i][j] in boxes_set[(i//3,j//3)]):
                    return False
                rows_set[i].add(board[i][j])
                cols_set[j].add(board[i][j])
                boxes_set[(i//3,j//3)].add(board[i][j])
        
        return True