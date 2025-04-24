# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self, root):
        current = root
        while current and current.left:
            current = current.left

        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base-case
        if not root: 
            return root
        
        # recursive case
        # search for node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # found node 
            # target node has 0 or 1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # has 2 children
                # find minimum value of the right subtree from this root
                # assign root to minimum value
                # remove the old minimum value in the right subtree from this root
                # assign root.right to new right subtree 
                min = self.find_min(root.right).val
                root.val = min
                root.right = self.deleteNode(root.right, min)
       
        return root
        