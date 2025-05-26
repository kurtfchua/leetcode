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
        
        self.res = [""]
        def iterative():
            for digit in digits: 
                tmp = []
                for combo in res: 
                    for c in keyboard[digit]:
                        tmp.append(combo+c)
                self.res = tmp
        res = []
        def dfs(i, curr_str):
            if len(curr_str) == len(digits): 
                res.append(curr_str)
                return 
            
            for c in keyboard[digits[i]]:
                dfs(i+1, curr_str+c)
        
        dfs(0, "")
        return res

            