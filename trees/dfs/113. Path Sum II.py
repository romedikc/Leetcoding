# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, curr_sum, curr_path, paths):
            if not root:
                return []
            curr_sum += root.val
            curr_path.append(root.val)

            if not root.left and not root.right and curr_sum == targetSum:
                paths.append(curr_path[:])

            dfs(root.left, curr_sum, curr_path, paths)
            dfs(root.right, curr_sum, curr_path, paths)

            curr_path.pop()  # pop current path to explore other paths

            return paths

        paths = []
        return dfs(root, 0, [], paths)
