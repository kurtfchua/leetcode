class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0

        for c in s: 
            if c in seen:
                seen.remove(c)
                length += 2
            else:
                seen.add(c)
        
        return length + 1 if seen else length
        