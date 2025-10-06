class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        n = len(g)
        best = [[inf for _ in range(n)] for _ in range(n)]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = inf

        def dfs(r, c, t):
            nonlocal ans
            if r == c == n - 1:
                ans = min(ans, t)
                return

            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nr < 0 or nr == n or nc < 0 or nc == n:
                    continue
                new_t = max(t, g[nr][nc])
                if new_t < best[nr][nc] and new_t < ans:
                    best[nr][nc] = new_t
                    dfs(nr, nc, new_t)

        dfs(0, 0, g[0][0])

        return ans
