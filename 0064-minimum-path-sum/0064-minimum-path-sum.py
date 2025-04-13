class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(m - 2, -1, -1):
            grid[n - 1][i] += grid[n - 1][i + 1]
        for i in range(n - 2, -1, -1):
            grid[i][m - 1] += grid[i + 1][m - 1]

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]
