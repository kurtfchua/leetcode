# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []
        def dfs(root):
            if not root: return 

            path.append(root.val)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        heapq.heapify(path)
        res = 0
        for _ in range(k):
            res = heapq.heappop(path)
        
        return res
        