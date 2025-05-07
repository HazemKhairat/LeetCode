from queue import PriorityQueue


class Solution:
    def minTimeToReach(self, mv: List[List[int]]) -> int:
        n, m = len(mv), len(mv[0])
        vis = [[float("inf")] * m for _ in range(n)]

        pq = PriorityQueue()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pq.put([0, 0, 0])
        vis[0][0] = 0

        while not pq.empty():
            curr = pq.get()
            t, r, c = curr[0], curr[1], curr[2]
            if r == n - 1 and c == m - 1:
                return t

            for dir in dirs:
                newR, newC = r + dir[0], c + dir[1]
                if newR < 0 or newC < 0 or newR == n or newC == m:
                    continue
                newT = max(t + 1, mv[newR][newC] + 1)
                if newT < vis[newR][newC]:
                    vis[newR][newC] = newT
                    pq.put((newT, newR, newC))

        return -1
