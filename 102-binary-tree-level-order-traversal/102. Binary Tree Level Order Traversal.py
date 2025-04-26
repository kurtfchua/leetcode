from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        levels = []
        
        if not root:
            return []
      
        queue.append(root)
        
        while queue:  
            children = []
            for i in range(len(queue)):
                current = queue.popleft()
                children.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
          
            levels.append(children)
        
        return levels
            
        