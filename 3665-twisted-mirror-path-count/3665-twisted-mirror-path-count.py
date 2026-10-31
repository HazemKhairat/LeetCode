class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])
        dp = {}

        def solve(r, c, lastDir):
            if r >= n or c >= m:
                return 0
            if r == n - 1 and c == m - 1:
                return 1

            if (r, c, lastDir) in dp:
                return dp[(r, c, lastDir)]

            ans = 0
            if grid[r][c] == 1:
                if lastDir == "r":
                    ans += solve(r + 1, c, "d")
                else:
                    ans += solve(r, c + 1, "r")
            else:
                ans += solve(r, c + 1, "r") + solve(r + 1, c, "d")

            dp[(r, c, lastDir)] = ans % MOD

            return ans % MOD

        return solve(0, 0, "")
