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
        
        def bfs(root):
            queue = deque()
            min_val, max_val = float('-inf'), float('inf')
            queue.append((root, min_val, max_val))

            while queue: 
                for i in range(len(queue)):
                    node, min_val, max_val = queue.popleft()
                    if node:
                        if not (min_val < node.val < max_val):
                            return False
                        
                        queue.append((node.left, min_val, node.val))
                        queue.append((node.right, node.val, max_val))
            
            return True

        #return dfs(root, float('-inf'), float('inf'))
        return bfs(root)