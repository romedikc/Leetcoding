# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, count):
            nonlocal max_length
            if not node:
                return
            max_length = max(max_length, count)
            if direction == "left":
                dfs(node.left, "right", count + 1)
                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", count + 1)
                dfs(node.left, "right", 1)

        max_length = 0
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        return max_length
