# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def solve(root):
            nonlocal ans
            if root == None:
                return 0

            left = solve(root.left)
            right = solve(root.right)
            curr = root.val
            if root.left:
                root.val += root.left.val
            if root.right:
                root.val += root.right.val

            if root.val // (left + right + 1) == curr:
                ans += 1

            return left + right + 1

        solve(root)
        return ans
