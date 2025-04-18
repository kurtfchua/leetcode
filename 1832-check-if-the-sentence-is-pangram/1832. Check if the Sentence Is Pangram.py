class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # go through each c in sentence
        # if c not in set add to set 
        # if set's size is 26 return true otherwise return false
        alpha_set = set()

        for c in sentence: 
            if c not in alpha_set:
                alpha_set.add(c)
        
        return len(alpha_set) == 26

        # T O(n) worst case we iterate through entire list to find all letters
        # S O(1) set may never grow past size 26

        