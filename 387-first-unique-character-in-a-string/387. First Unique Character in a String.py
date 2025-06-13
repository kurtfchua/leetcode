class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]][0] += 1
            else:
                hashmap[s[i]] = [1, i] 
        
        min_index = float('inf')

        for k, v in hashmap.items():
            if v[0] == 1:
                min_index = min(min_index, v[1])
        
        return min_index if min_index != float('inf') else -1
        