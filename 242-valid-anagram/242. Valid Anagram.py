class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hashmap = defaultdict(int)
        
        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        
        for c, count in hashmap.items():
            if count != 0:
                return False
        
        return True