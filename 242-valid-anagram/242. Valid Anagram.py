class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 dictionaries, where freq of each char in s and t are counted
        # if dictionaries are equal then they are anagrams 
        s_dict = {}
        t_dict = {}

        for c in s: 
            s_dict[c] = s_dict.get(c, 0) + 1
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
            
        return s_dict == t_dict


        