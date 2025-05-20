# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_level, max_level):
            if not root: return True

            if not (min_level < root.val < max_level):
                return False
            
            return dfs(root.left, min_level, root.val) and dfs(root.right, root.val, max_level)
        
        return dfs(root, float('-inf'), float('inf'))