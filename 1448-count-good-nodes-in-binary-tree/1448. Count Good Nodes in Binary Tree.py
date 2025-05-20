# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def bfs(root, count):
            queue = deque()
            queue.append((root, root.val))

            while queue:
                for i in range(len(queue)):
                    node, max_so_far = queue.popleft()
                    if node:
                        if node.val >= max_so_far:
                            count += 1
                        max_so_far = max(max_so_far, node.val)
                        queue.append((node.left, max_so_far))  
                        queue.append((node.right, max_so_far))
            return count  

        def dfs(root, max_val):
            if not root: return 0 

            res = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)
            res += dfs(root.left, max_val) + dfs(root.right, max_val)          

            return res
            
        #return bfs(root, 0)
        return dfs(root, root.val)