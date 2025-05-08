class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_left, max_right = height[l], height[r]
        count = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left,height[l])
                count += max_left - height[l]
            else:
                r-=1
                max_right = max(max_right,height[r])
                count += max_right-height[r]
        return count

        # T O(n): we use 2 pointers to reach each element in height at most once
        # S O(1): we iterate in place using 2 pointers, no new data structures were used


        