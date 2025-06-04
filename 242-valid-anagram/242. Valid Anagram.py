class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_chars = [0]*26
        t_chars = [0]*26

        for c in s: 
            s_chars[ord(c)-ord('a')] += 1
        
        for c in t: 
            t_chars[ord(c)-ord('a')] += 1

        return s_chars == t_chars