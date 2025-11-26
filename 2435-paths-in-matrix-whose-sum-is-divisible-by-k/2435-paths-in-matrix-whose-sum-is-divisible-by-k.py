class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        n, m = len(grid), len(grid[0])
        memo = {}

        def solve(r, c, rem):
            if (r == n or c == m):
                return 0
            if r == n - 1 and c == m - 1:
                return ((rem + grid[r][c]) % k) == 0
            
            if (r, c, rem) in memo:
                return memo[(r, c, rem)]
            
            down = solve(r + 1, c, (rem + grid[r][c]) % k)
            right = solve(r, c + 1, (rem + grid[r][c]) % k)
            memo[(r, c, rem)] = (down + right) % mod
            return (down + right) % mod

        return solve(0, 0, 0) % mod
              