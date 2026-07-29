#py3
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return 0
            left = bfs(root.left)
            if left == -1 : return -1

            right = bfs(root.right)
            if right == -1 : return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left , right)
        return bfs(root) != -1