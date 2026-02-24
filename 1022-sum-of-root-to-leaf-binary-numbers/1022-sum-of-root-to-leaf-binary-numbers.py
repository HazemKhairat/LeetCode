# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def solve(root, binNum):
            if not root:
                return 0
            elif not root.left and not root.right:
                return int(binNum + str(root.val), 2)

            left = solve(root.left, binNum + str(root.val))
            right = solve(root.right, binNum + str(root.val))
            return left + right

        return solve(root, "")
