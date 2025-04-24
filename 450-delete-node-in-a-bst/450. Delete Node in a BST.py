# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self,root):
        current = root
        while current and current.left:
            current = current.left

        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # 2 children
                min_val = self.find_min(root.right).val # find min in right subtree from root
                root.val = min_val# assign root value to min
                root.right = self.deleteNode(root.right, min_val) # remove the min value from right subtree
        
        return root

        
        