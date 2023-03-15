# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = [root]
        found_none = False  # if we have found a None node in the level
        while queue:
            levels = []
            for i in range(len(queue)):
                node = queue.pop(0)
                levels.append(node.val)

                if found_none and (node.left or node.right):
                    return False
                if not node.left and node.right:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # if either child is missing,
                # we have found a None node in this level
                if not node.left or not node.right:
                    found_none = True
        return True
