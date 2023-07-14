# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, curr_max):
            if not root:
                return 0
            # Check if the current node is a good node
            if root.val >= curr_max:
                count = 1
            else:
                count = 0
            # Update the maximum value for the path to the current node
            curr_max = max(curr_max, root.val)

            # Recursively traverse the left and right subtrees, and add the counts
            count += dfs(root.left, curr_max)
            count += dfs(root.right, curr_max)
            return count

        return dfs(root, root.val)
