class Solution:

    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n, m = len(t1), len(t2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = 1 + dp[i][j] if t1[i] == t2[j] else max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]
