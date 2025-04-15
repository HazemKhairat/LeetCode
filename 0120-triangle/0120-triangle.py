class Solution:
    def minimumTotal(self, dp: List[List[int]]) -> int:
        n = len(dp)
        for i in range(n - 2, -1, -1):
            for j in range(len(dp[i]) - 1, -1, -1):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
