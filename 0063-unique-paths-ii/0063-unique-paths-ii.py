class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        n, m = len(obs), len(obs[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            if i == n or j == m or obs[i][j] == 1:
                return 0
            if i == n - 1 and j == m - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            dp[i][j] = down + right
            return dp[i][j]

        return dfs(0, 0)
