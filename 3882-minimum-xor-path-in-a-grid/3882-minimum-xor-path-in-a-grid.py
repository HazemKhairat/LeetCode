class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        ans = inf
        n, m = len(grid), len(grid[0])

        dp = [[[False] * 1025 for _ in range(m)] for _ in range(n)]
        
        def dfs(r, c, xor):
            nonlocal ans
            if r == n or c == m or r < 0 or c < 0 or dp[r][c][xor]:
                return

            if r == n - 1 and c == m - 1:
                ans = min(ans, xor ^ grid[r][c])
                return

            dfs(r, c + 1, xor ^ grid[r][c])
            dfs(r + 1, c, xor ^ grid[r][c])
            dp[r][c][xor] = True

        dfs(0, 0, 0)

        return ans
