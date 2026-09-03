class Solution:
    def minMoves(self, grid: List[str], energy: int) -> int:
        n, m = len(grid), len(grid[0])
        ids = [[0] * m for _ in range(n)]
        cnt = 0
        sr, sc = -1, -1

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "S":
                    sr, sc = r, c
                if grid[r][c] == "L":
                    ids[r][c] = cnt
                    cnt += 1

        masks = 1 << cnt
        fullMask = masks - 1
        best = [[[-1] * (masks) for _ in range(m)] for _ in range(n)]
        # print(best)
        q = deque()
        q.append((sr, sc, energy, 0, 0))  # r, c, e, mask, dist
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            r, c, en, mask, dist = q.popleft()

            if mask == fullMask:
                return dist
            if en == 0:
                continue

            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if grid[nr][nc] == "X":
                    continue

                newMask = mask
                newEn = en - 1

                if grid[nr][nc] == "L":
                    newMask |= 1 << ids[nr][nc]

                if grid[nr][nc] == "R":
                    newEn = energy
                if best[nr][nc][newMask] >= newEn:
                    continue
                best[nr][nc][newMask] = newEn
                q.append((nr, nc, newEn, newMask, dist + 1))

        return -1
