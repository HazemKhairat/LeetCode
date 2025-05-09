from queue import PriorityQueue


class Solution:
    def minTimeToReach(self, mv: List[List[int]]) -> int:
        n, m = len(mv), len(mv[0])
        vis = [[float("inf")] * m for _ in range(n)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pq = PriorityQueue()

        pq.put((0, 0, 0, 0))  # time, row, col, next

        while not pq.empty():
            t, r, c, nextMove = pq.get()

            if t >= vis[r][c]:
                continue
            vis[r][c] = t

            if r == n - 1 and c == m - 1:
                return t

            for lr, lc in dirs:
                nr, nc = lr + r, lc + c

                if nr < 0 or nr == n or nc < 0 or nc == m:
                    continue

                flag = 2 if nextMove == 1 else 1

                newT = max(t + flag, mv[nr][nc] + flag)

                if r == 0 and c == 0 and mv[nr][nc] <= t:
                    newT = flag + mv[nr][nc]

                if newT < vis[nr][nc]:
                    pq.put((newT, nr, nc, flag))

        return -1
