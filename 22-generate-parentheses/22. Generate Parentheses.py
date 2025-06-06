class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(opened, closed):
            if opened == n and closed == n:
                res.append("".join(subset.copy()))
                return 
            
            if opened < n: 
                subset.append("(")
                dfs(opened+1, closed)
                subset.pop()

            if closed < opened: 
                subset.append(")")
                dfs(opened, closed+1)
                subset.pop()
            
        dfs(0,0)

        return res 
        

