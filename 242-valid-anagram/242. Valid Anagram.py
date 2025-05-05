class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_freq = {}

        for c in s: 
            s_freq[c] = s_freq.get(c, 0) + 1
        
        for c in t: 
            if c not in s_freq:
                return False
            s_freq[c] -= 1
        
        for v in s_freq.values():
            if v != 0:
                return False
        
        return True

        # T O(m+n) - we must iterate through both strings to see if they are anagrams of each other. 
        # S O(m) - we create a hashmap as large as string s
        