class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26

        for c in s:
            counts[ord(c)-ord('a')]+=1
        
        for c in t:
            index = ord(c)-ord('a')
            if counts[index] < 0:
                return False
            counts[index] -= 1
        
        return not any(counts)
        