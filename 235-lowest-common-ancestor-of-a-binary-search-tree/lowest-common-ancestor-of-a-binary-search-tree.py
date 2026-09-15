# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        
        if root.val > p.val and root.val > q.val:  # agar root.val p.val and q.val sa greater hai too  left ma jayga
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val and root.val < q.val:  # agar root.val p.val and q.val sa small  hai too  right  ma jayga
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root


        