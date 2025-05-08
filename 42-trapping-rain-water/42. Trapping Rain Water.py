class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = deque()
        max_left = 0
        max_right = 0

        for i in range(len(height)):
            prefix.append(max_left)
            max_left = max(max_left,height[i])

        for i in range(len(height)-1,-1,-1):
            suffix.appendleft(max_right)
            max_right = max(max_right, height[i])
        list(suffix)

        count = 0
        for i in range(len(height)):
            if min(prefix[i],suffix[i])-height[i] <=0:
                continue
            count+= min(prefix[i],suffix[i])-height[i]
        
        return count

        # T O(n): we have to iterate through height to build the prefix and suffix lists and then get count
        # S O(n): we build prefix and suffix lists that grow lineraly with the input

