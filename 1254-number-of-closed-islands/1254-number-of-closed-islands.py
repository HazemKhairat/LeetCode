class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        n, m = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m:
                return False

            if grid[r][c] == 1 or (r, c) in visited:
                return True

            visited.add((r, c))
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            top = dfs(r - 1, c)
            down = dfs(r + 1, c)

            return left and right and top and down

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 and (r, c) not in visited:
                    ans += dfs(r, c)

        return ans
