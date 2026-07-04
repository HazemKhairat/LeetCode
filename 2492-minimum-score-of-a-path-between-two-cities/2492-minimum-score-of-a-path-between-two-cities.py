class DSU:

    def __init__(self, size):
        self.size = size
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        dsu = DSU(n + 1)

        for u, v, c in roads:
            dsu.union(u, v)

        ans = inf
        for u, v, c in roads:
            if dsu.find(v) == 1:
                ans = min(ans, c)

        return ans
