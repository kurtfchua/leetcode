class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict, magazine_dict = {} , {}

        for c in ransomNote:
            if c not in ransom_dict:
                ransom_dict[c] = 1
            else:
                ransom_dict[c] = ransom_dict[c] + 1
        
        for c in magazine:
            if c not in magazine_dict:
                magazine_dict[c] = 1
            else:
                magazine_dict[c] = magazine_dict[c] + 1
        
        for key in ransom_dict:
            if key not in magazine_dict:
                return False
            if ransom_dict[key] > magazine_dict[key]:
                return False
        
        return True

        
