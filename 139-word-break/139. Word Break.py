class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True
            
            for word in wordDict:
                if (i+len(word) <= len(s) and 
                    s[i:i+len(word)] == word):
                    if dfs(i+len(word)): 
                        return True
            
            return False
        
        #return dfs(0)
        mem = {}
        def top_down(i):
            if i == len(s):
                return True
            if i in mem:
                return mem[i]
            
            for word in wordDict: 
                if (i + len(word) <= len(s) and 
                    s[i:i+len(word)] == word):
                    if top_down(i+len(word)):
                        mem[i] = True
                        return True
            
            mem[i] = False
            return False
        
        return top_down(0)