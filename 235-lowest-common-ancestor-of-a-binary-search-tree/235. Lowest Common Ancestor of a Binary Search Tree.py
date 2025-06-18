# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bst left child is less and right child is more than its parent
        # have lca as root by default 
        # if both values are less than the lca then their ancestor exists in the left subtree
        # if both values are greater than the lca then their ancestor exists in the right subtree
        
        lca = root
        while lca: 
            if p.val < lca.val and q.val < lca.val: 
                lca = lca.left
            elif p.val > lca. val and q.val > lca.val:
                lca = lca.right
            else:
                return lca