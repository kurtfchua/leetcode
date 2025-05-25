class TrieNode: 

    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words: 
            curr = root
            for c in word: 
                if c not in curr.children: 
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word
        
        rows, cols = len(board), len(board[0])
       
        def dfs(r, c, root):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] == "#"):
                return 
            
            if board[r][c] not in root.children: 
                return 
            
            next_node = root.children[board[r][c]]

            if next_node.word: 
                res.add(next_node.word)
            
            tmp = board[r][c]
            board[r][c] = "#"

            dfs(r+1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c-1, next_node)

            board[r][c] = tmp
        
        res = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children: 
                    dfs(r, c, root)
        
        return list(res)
        