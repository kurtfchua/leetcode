class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}

        for c in s: 
            if c in s_freq:
                s_freq[c] += 1
            else:
                s_freq[c] = 1
        
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
        