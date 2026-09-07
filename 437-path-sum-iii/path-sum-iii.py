# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum += node.val
            if current_sum == targetSum:
                total_path = 1
            else:
                total_path = 0

            total_path += dfs(node.left, current_sum)
            total_path += dfs(node.right, current_sum)

            return total_path

        def count_paths(node):
            if not node:
                return 0
            total_paths = dfs(node, 0)
            total_paths += count_paths(node.left)
            total_paths += count_paths(node.right)
            return total_paths

        return count_paths(root)
        