class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = Counter(s1)
        counts2 = Counter()
        for i in range(len(s2)):
            counts2[s2[i]] += 1
            if i >= len(s1):
                left_c = s2[i-len(s1)]
                if counts2[left_c] == 1:
                    del counts2[left_c]
                else:
                    counts2[left_c] -= 1
            
            if counts1 == counts2:
                return True
        
        return False

        