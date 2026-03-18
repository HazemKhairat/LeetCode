class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        for c in range(1, m):
            grid[0][c] += grid[0][c - 1]
        for r in range(1, n):
            grid[r][0] += grid[r - 1][0]

        for r in range(1, n):
            for c in range(1, m):
                grid[r][c] += grid[r - 1][c] + grid[r][c - 1] - grid[r - 1][c - 1]


        ans= 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] <= k:
                    ans += 1
        return ans