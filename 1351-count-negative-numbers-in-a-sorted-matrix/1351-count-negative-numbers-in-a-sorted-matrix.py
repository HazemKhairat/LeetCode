class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        i, j = n - 1, 0
        res = 0

        while i >= 0 and j < m:
            if grid[i][j] < 0:
                res += m - j
                i -= 1
            else:
                j += 1
        
        return res