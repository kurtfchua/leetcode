class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26

        for i in range(len(s)): 
            char_count[ord(s[i])-ord('a')] += 1
            char_count[ord(t[i])-ord('a')] -= 1

        for c in char_count: 
            if c != 0: 
                return False
        
        return True

        