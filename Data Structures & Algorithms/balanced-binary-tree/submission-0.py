# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def dfs(root, d):

            if not root:
                return 0

            l = dfs(root.left, d + 1)
            r = dfs(root.right, d + 1)
            
            if abs(l - r) > 1:
                self.ans = False
            
            return 1 + max(l, r)
        
        dfs(root, 0)
        return self.ans

            
        
        
        