# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def bf(preorder, inorder):
            if not preorder or not inorder: return None

            root = TreeNode(preorder[0])
            root_idx = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
            root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
            

            return root        
        
        hashmap = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0 
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(root_val)
            inorder_idx = hashmap[root_val]
            root.left = dfs(l, inorder_idx-1)
            root.right = dfs(inorder_idx+1, r)

            return root
        
        return dfs(0, len(inorder)-1)