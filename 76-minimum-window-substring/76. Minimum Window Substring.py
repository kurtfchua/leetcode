class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        t_counts, window_counts = Counter(t), {}
        have, need = 0, len(t_counts)
        res, res_length = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            window_counts[s[r]] = window_counts.get(s[r],0) + 1
            if s[r] in t_counts and window_counts[s[r]] == t_counts[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < res_length:
                    res, res_length = [l, r], r-l+1
                window_counts[s[l]] -= 1
                if s[l] in t_counts and window_counts[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1 
        l, r = res
        
        return s[l:r+1] if res_length != float('inf') else ""