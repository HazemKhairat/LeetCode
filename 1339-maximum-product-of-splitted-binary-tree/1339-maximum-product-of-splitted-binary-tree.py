class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(root):
            if root == None:
                return 0
            root.val += dfs(root.left) + dfs(root.right)
            return root.val

        dfs(root)

        maxi = 0
        total = root.val

        def solve(root):
            nonlocal maxi
            if root == None:
                return
            solve(root.left)
            solve(root.right)
            maxi = max(maxi, root.val * (total - root.val))

        solve(root)
        return maxi % MOD
