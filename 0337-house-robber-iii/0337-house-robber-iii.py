class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def solve(root, taken):
            if not root:
                return 0

            key = (root, taken)
            if key in dp:
                return dp[key]

            take = skip = 0
            if taken == False:
                take = root.val + solve(root.left, True) + solve(root.right, True)

            skip = solve(root.left, False) + solve(root.right, False)
            dp[key] = max(take, skip)
            return dp[key]

        return solve(root, False)
