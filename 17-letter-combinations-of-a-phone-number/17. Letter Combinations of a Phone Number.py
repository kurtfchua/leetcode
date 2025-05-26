class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]
        for digit in digits: 
            tmp = []
            for combo in res: 
                for c in keyboard[digit]:
                    tmp.append(combo+c)
            res = tmp

        return res
        