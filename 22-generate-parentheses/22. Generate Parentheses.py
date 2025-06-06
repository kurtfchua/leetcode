class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combination = []

        def dfs(opened, closed):
            if opened == closed == n: 
                res.append("".join(combination))
                return 
            
            if opened < n: 
                combination.append("(")
                dfs(opened+1, closed)
                combination.pop()
            
            if closed < opened: 
                combination.append(")")
                dfs(opened, closed+1)
                combination.pop()

        dfs(0,0)

        return res

        