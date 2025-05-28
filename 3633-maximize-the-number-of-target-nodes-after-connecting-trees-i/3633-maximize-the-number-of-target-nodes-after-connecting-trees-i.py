class Solution:

    def dfs(self, node, k, tree, vis):
        if k <= 0:
            return 0
        vis.add(node)
        sum = 0
        for nighbour in tree[node]:
            if nighbour in vis:
                continue

            sum += 1 + self.dfs(nighbour, k - 1, tree, vis)

        return sum

    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        if k == 0:
            return [1] * n
            
        tree1 = [[] for _ in range(n)]
        tree2 = [[] for _ in range(m)]

        for edge in edges1:
            a, b = edge
            tree1[a].append(b)
            tree1[b].append(a)

        for edge in edges2:
            u, v = edge
            tree2[u].append(v)
            tree2[v].append(u)


        res = [0] * n

        maxi = 0
        for j in range(m):
            vis2 = set()
            maxi = max(maxi, self.dfs(j, k - 1, tree2, vis2) + 1)
            
        for i in range(n):
            vis = set()
            sum = self.dfs(i, k, tree1, vis) + 1
            
            res[i] = sum + maxi

        return res
