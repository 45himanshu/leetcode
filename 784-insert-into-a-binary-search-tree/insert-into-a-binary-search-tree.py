# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val = val)
        if root is None:
            root = new_node
            return root
        current = root

        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    return root
                current = current.left
            
            else:
                if current.right is None:
                    current.right = new_node
                    return root
                current = current.right
        