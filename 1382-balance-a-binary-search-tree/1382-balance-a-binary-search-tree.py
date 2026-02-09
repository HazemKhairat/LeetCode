# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inOrderTravers(root):
            if root == None:
                return

            inOrderTravers(root.left)
            arr.append(root.val)
            inOrderTravers(root.right)

        inOrderTravers(root)

        def balanceArr(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            left = balanceArr(l, mid - 1)
            right = balanceArr(mid + 1, r)
            return TreeNode(arr[mid], left, right)

        return balanceArr(0, len(arr) - 1)
