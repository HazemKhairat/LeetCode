class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        maxi, ans, level = -inf, 0, 1
        while q:
            n = len(q)
            curr_sum = 0
            for i in range(n):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxi < curr_sum:
                ans, maxi = level, curr_sum
            level += 1

        return ans
