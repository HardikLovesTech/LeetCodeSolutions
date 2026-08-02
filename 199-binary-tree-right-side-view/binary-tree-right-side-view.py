# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderTraversal(self , root):
        if not root:
            return 
        tree = []
        q = deque([root])

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            tree.append(level)
        
        return tree
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        lvl = self.levelOrderTraversal(root)
        bs = []
        for i in range(len(lvl)):

            bs.append(lvl[i][-1])
        
        return bs