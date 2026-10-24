# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i+=1

        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root





        # # 3 approch 
        # index = 0
        # def bst_helper(preorder, boundary):
        #     nonlocal index
        #     if index >= len(preorder) or preorder[index] > boundary:
        #         return None

        #     n = TreeNode(preorder[index])
        #     index+=1

        #     n.left = bst.helper(preorder, n.val)
        #     n.right = bst_helper(preoder, boundary)

        #     return n

        #     return bst_helper(preorder, float('info'))
        