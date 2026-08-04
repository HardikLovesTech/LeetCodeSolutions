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
        def dfs(node , mv):
            if not node:
                return 0
            good = 0
            if node.val >= mv:
                good+=1 
                mv = node.val
            return (good + dfs(node.right , mv) + dfs(node.left , mv))
        return dfs(root , root.val)