class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

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
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        edges.sort(key=lambda x: -x[2])
        mst = []

        for edge in edges:
            if edge[-1] == 1:
                if dsu.find(edge[0]) == dsu.find(edge[1]):
                    return -1
                dsu.union(edge[0], edge[1])
                mst.append(edge)

        for edge in edges:
            if len(mst) == n - 1:
                break
            if edge[-1] == 0:
                if dsu.find(edge[0]) != dsu.find(edge[1]):
                    dsu.union(edge[0], edge[1])
                    mst.append(edge)

        if len(mst) != n - 1:
            return -1
            
        mst.sort(key=lambda x: x[2])
        for edge in mst:
            if k == 0:
                break
            if edge[-1] == 0:
                edge[2] *= 2
                k -= 1

        mst.sort(key=lambda x: x[2])
        return mst[0][2]
