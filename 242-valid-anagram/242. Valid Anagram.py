class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary holding the counts for the first string
        # now iterate through the second string subtracting the value in the dict by 1
        # if value is at 0 or value doesn't exist it is not an anagram
        # otherwise return True
        s_dict = {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        
        for c in t:
            if c not in s_dict or s_dict[c] == 0: 
                return False
            s_dict[c] -=1
        
        for val in s_dict.values():
            if val != 0:
                return False
                
        return True


        