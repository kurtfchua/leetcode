class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26

        for c in s:
            counts[ord(c)-ord('a')] += 1

        for c in t:
            counts[ord(c)-ord('a')] -= 1        
            if counts[ord(c)-ord('a')] < 0:
                return False
        
        for count in counts:
            if count != 0:
                return False
        return True