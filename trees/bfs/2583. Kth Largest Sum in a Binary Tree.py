# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        queue = [root]
        res = []
        while queue:
            levels = []
            for i in range(len(queue)):
                node = queue.pop(0)
                levels.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum(levels))

        if k > len(res):
            return -1

        # Sort the level sums in descending order
        res.sort(reverse=True)

        return res[k - 1]
