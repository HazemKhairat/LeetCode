# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_arr = []

        def traverse(root):
            if not root:
                return

            traverse(root.left)
            sorted_arr.append(root.val)
            traverse(root.right)

        traverse(root)

        def balanced_bst(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            left_subTree = balanced_bst(l, mid - 1)
            right_subTree = balanced_bst(mid + 1, r)
            return TreeNode(sorted_arr[mid], left_subTree, right_subTree)

        return balanced_bst(0, len(sorted_arr) - 1)
