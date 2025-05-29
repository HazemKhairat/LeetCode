class Solution:

    def BFS(self, tree):
        n = len(tree)
        q = deque()
        q.append(0)
        colors = [False] * (n)
        colors[0] = True
        vis = [False] * (n)
        vis[0] = True

        while q:
            node = q.popleft()
            for nighbour in tree[node]:
                if not vis[nighbour]:
                    colors[nighbour] = not colors[node]
                    q.append(nighbour)
                    vis[nighbour] = True
        return colors

    def build(self, edges):
        n = len(edges)
        tree = [[] for _ in range(n + 1)]
        for edge in edges:
            u, v = edge
            tree[u].append(v)
            tree[v].append(u)
        
        return tree

    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        n, m = len(edges1), len(edges2)

        tree1 = self.build(edges1)
        tree2 = self.build(edges2)

        colors1 = self.BFS(tree1)
        colors2 = self.BFS(tree2)

        even = sum(colors1)
        odd = n - even + 1

        temp = sum(colors2)
        maxi = max(temp, m + 1 - temp)

        res = [0] * (n + 1)
        for i in range(n + 1):
            if colors1[i]:
                res[i] = even + maxi
            else:
                res[i] = odd + maxi

        return res
