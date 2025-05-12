class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i-prev_index))
                start = prev_index
            stack.append([start, h])

        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (len(heights)-index))
            
        return max_area
        