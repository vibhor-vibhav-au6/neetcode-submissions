# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def depth(root, d):
            if not root:
                return 0

            l = depth(root.left, d + 1)
            r = depth(root.right, d + 1)

            self.dia = max(self.dia, l + r)

            return 1 + max (l, r)

        depth(root, 0)

        return self.dia