# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return root
            
            root.left, root.right = root.right, root.left

            dfs(root.left)
            dfs(root.right)
        
        def bfs(root):
            queue = deque([root])
            visited = set([root])

            while queue: 
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node: 
                        node.left, node.right = node.right, node.left
                        queue.append(node.left)
                        queue.append(node.right)
                        visited.add(node.left)
                        visited.add(node.right)
        
        #dfs(root)
        bfs(root)
        return root
        