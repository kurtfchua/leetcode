# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root: return root

            queue = deque()
            queue.append(root)
            path = []
            while queue: 
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        path.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        path.append(None)
            return path
        return bfs(p) == bfs(q)
        