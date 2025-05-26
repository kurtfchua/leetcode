class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                if is_palindrome(s,i,j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        
        def is_palindrome(s, i, j):
            while i < j: 
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        dfs(0)

        return res