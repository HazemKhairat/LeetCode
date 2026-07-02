class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:

        n, m = len(grid), len(grid[0])
        vis = set()

        dp = [[[-1] * (h + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        def solve(r, c, h):

            if h <= 0 or r < 0 or r >= n or c < 0 or c >= m or (r, c) in vis:
                return False

            if r == n - 1 and c == m - 1:
                return h - grid[r][c] > 0

            if dp[r][c][h] != -1:
                return dp[r][c][h]

            vis.add((r, c))
            left = solve(r, c - 1, h - grid[r][c])
            right = solve(r, c + 1, h - grid[r][c])
            top = solve(r - 1, c, h - grid[r][c])
            down = solve(r + 1, c, h - grid[r][c])
            vis.remove((r, c))

            dp[r][c][h] = left or right or top or down
            return dp[r][c][h]

        return solve(0, 0, h)
