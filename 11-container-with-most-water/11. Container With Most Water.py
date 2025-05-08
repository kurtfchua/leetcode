class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force: for every height iterate the rest of the list and multiply areas for it
        # area = min(l,r) * (r-l) -> update max 
        # optimal: two pointers l,r from 0..n. apply same algorithm but change pointer based on the smaller height. increment/decrement as needed

        i, j = 0, len(height)-1
        max_area = 0

        while i < j:
            area = min(height[i],height[j]) * (j-i)
            max_area = max(max_area,area)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_area

        # T O(n), S O(1)