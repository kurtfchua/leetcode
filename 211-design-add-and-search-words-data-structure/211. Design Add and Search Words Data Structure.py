class TrieNode: 
    
    def __init__(self): 
        self.children = {}
        self.is_last = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_last = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_last
            
            if word[index] == ".":
                for child in node.children.values(): 
                    if dfs(child, index+1): 
                        return True
                return False
            else: 
                if word[index] not in node.children: 
                    return False
                return dfs(node.children[word[index]], index + 1)
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)