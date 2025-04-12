class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def isValid(i, j):
            return False if i == n or j == m or i < 0 or j < 0 else True

        def dfs(i, j):
            if not isValid(i, j):
                return 0
            elif i == n - 1 and j == m - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            right = dfs(i + 1, j)
            down = dfs(i, j + 1)
            dp[i][j] = right + down
            return dp[i][j]

        return dfs(0, 0)
