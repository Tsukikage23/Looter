# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return 1 + max(l,r)
    def isBalanced(self, root):
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh-rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)