class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target: 
                res.append(subset.copy())
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            subset.append(candidates[i])
            dfs(i, total + candidates[i])

            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return res        