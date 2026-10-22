# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node):
            nonlocal current_sum

            if not node:
                return

            dfs(node.right)

            current_sum += node.val
            node.val = current_sum

            dfs(node.left)

        current_sum = 0
        dfs(root)
        return root


        