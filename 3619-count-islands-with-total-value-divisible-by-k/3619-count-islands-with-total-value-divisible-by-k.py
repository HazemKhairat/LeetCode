class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0:
                return 0

            sum_ = grid[r][c]
            grid[r][c] = 0
            sum_ += dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return sum_

        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    res = dfs(r, c)
                    if res % k == 0:
                        ans += 1

        return ans
