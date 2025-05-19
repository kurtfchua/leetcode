# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root

        while lca:
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left
            elif p.val > lca.val and q.val > lca.val:
                lca = lca.right
            else:
                return lca
        