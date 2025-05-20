# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, depth):
            if not root: return 

            if depth == len(res):
                res.append(root.val)
            
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        def bfs(root):
            queue = deque()
            queue.append(root)

            while queue:
                right_view = None
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        right_view = node
                        queue.append(node.left)
                        queue.append(node.right)
                if right_view:
                    res.append(right_view.val)
        
        #dfs(root, 0)
        bfs(root)
        return res
        