# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node,sum1):
            if not node:
                return False
            sum1 += node.val
            if not node.left and not node.right:
                return sum1 == targetSum
            
            return dfs(node.left,sum1) or dfs(node.right,sum1)
        return dfs(root,0)