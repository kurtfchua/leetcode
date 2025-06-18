class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in range(len(s)):
            if s[i] not in map: 
                map[s[i]] = (i, 1)
            else:
                map[s[i]] = (map[s[i]][0],map[s[i]][1]+1)
        
        
    
        for l in map: 
            if map[l][1] == 1: 
                return map[l][0]
        return -1
        