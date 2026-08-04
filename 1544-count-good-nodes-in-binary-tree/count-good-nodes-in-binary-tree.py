# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node , max_v):
            if not node:
                return 0
            good = 0
            if node.val >= max_v:
                good+= 1
                max_v = node.val
            return (
                good + dfs(node.left , max_v) + dfs(node.right , max_v)
            )
        return dfs(root , root.val)