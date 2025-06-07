class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][0]:
                prev_h, prev_i = stack.pop()
                max_area = max(max_area, prev_h * (i-prev_i))
                start = prev_i
            
            stack.append((h, start))
        
        while stack: 
            h, i = stack.pop()
            max_area = max(max_area, h * (len(heights)-i))
        
        return max_area
        