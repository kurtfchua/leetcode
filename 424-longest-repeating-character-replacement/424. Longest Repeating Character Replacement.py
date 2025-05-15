class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        res = 0
        max_freq = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r],0) + 1
            max_freq = max(max_freq, counts[s[r]])
            while (r-l+1) - max_freq > k:
                counts[s[l]] -= 1
                l +=1
            res = max(res, r-l+1)
        
        return res
        