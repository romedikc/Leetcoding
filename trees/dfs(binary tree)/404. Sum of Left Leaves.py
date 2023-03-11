# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(root, is_left):
            nonlocal total
            if not root:
                return 0
            dfs(root.left, True)
            dfs(root.right, False)
            # only adding left leaves
            if not root.left and not root.right and is_left:
                total += root.val

        dfs(root, False)
        return total



