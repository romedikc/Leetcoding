"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        def dfs(root):
            if not root:
                return None
            for i in root.children:
                dfs(i)
            output.append(root.val)

        dfs(root)
        return output
