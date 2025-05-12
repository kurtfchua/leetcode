class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = i-prev_i
            stack.append([v,i])
        
        return res

        # T O(n), S O(n)
        