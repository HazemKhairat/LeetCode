# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(l, r):
            if l == r:
                return None
            maxi = findMax(l, r)
            root = TreeNode(nums[maxi])
            root.left = build(l, maxi)
            root.right = build(maxi + 1, r)

            return root

        def findMax(l, r):
            maxi = l
            for i in range(l, r):
                if nums[maxi] < nums[i]:
                    maxi = i
            return maxi
        
        return build(0, len(nums))
