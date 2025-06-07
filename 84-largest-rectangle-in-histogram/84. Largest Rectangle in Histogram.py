class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 

        for i, v in enumerate(heights): 
            start = i 
            while stack and v < stack[-1][0]:
                height, prev_idx = stack.pop()
                max_area = max(max_area, height * (i-prev_idx))
                start = prev_idx
            stack.append((v, start))
        
        while stack: 
            height, idx = stack.pop()
            max_area = max(max_area, height * (len(heights)-idx))
        
        return max_area
