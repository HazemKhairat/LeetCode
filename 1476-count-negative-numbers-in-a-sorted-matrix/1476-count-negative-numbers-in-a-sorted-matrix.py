class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        res = 0
        
        for i in range(n):
            l, r = 0, m - 1

            while l <= r:
                mid = (l + r) // 2
                if grid[i][mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            res += (m - l)

        return res
