# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        maxi = -inf
        ans = 0
        level = 1
        while q:
            n = len(q)
            tmp = 0
            for i in range(n):
                node = q.popleft()
                tmp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxi < tmp:
                ans = level
                maxi = tmp
            level += 1

        return ans
