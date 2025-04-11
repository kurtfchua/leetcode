class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 dictionaries, where freq of each char in s and t are counted
        # if dictionaries are equal then they are anagrams 
        s_dict = {}
        t_dict = {}

        for c in s: 
            if c in s_dict: 
                s_dict[c] +=1
            else:
                s_dict[c] = 1

        for c in t:
            if c in t_dict:
                t_dict[c] +=1
            else:
                t_dict[c] = 1
        
        return s_dict == t_dict


        