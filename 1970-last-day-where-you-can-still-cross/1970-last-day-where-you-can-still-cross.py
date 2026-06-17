class DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return

        if p1 < p2:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        arr = [[1] * col for _ in range(row)]
        n = row * col + 2
        dsu = DSU(n)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            id1 = r * col + c + 1
            arr[r][c] = 0
            for di in dirs:
                nr, nc = r + di[0], c + di[1]
                if 0 <= nr < row and 0 <= nc < col and arr[nr][nc] == 0:
                    id2 = nr * col + nc + 1
                    dsu.union(id1, id2)

            if r == 0:
                dsu.union(0, id1)
            if r == row - 1:
                dsu.union(row * col + 1, id1)

            if dsu.find(0) == dsu.find(row * col + 1):
                return i

        return 0
