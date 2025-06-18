class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts = [0]*26
        
        for c in s: 
            counts[ord(c)-ord('a')] += 1
        
        for c in t: 
            counts[ord(c)-ord('a')] -= 1
            if counts[ord(c)-ord('a')] < 0: 
                return False

        for c in counts: 
            if c != 0:
                return False
        
        return True
    