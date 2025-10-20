# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(l, root):
            if root == None:
                return l
            
            left = dfs(l + 1, root.left)
            right = dfs(l + 1, root.right)
            return max(left, right)
        
        return dfs(0, root)
