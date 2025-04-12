class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m + 1)] for _ in range(n)]
        dp[n - 1] = [1] * m

        for i in range(n - 2, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
