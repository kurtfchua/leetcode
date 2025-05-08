class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        max_left = 0
        max_right = 0

        for i in range(len(height)):
            prefix.append(max_left)
            max_left = max(max_left,height[i])

        for i in range(len(height)-1,-1,-1):
            suffix.append(max_right)
            max_right = max(max_right, height[i])
        suffix.reverse()

        count = 0
        for i in range(len(height)):
            if min(prefix[i],suffix[i])-height[i] <=0:
                continue
            count+= min(prefix[i],suffix[i])-height[i]
        
        return count


