class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:

        n = len(edges) + 1
        LOG = math.ceil(math.log2(n)) + 1
        tree = [[] for _ in range(n)]
        depth = [0] * (n + 1)
        up = [[-1] * LOG for _ in range(n)]
        MOD = 10**9 + 7

        for u, v in edges:
            tree[u - 1].append(v - 1)
            tree[v - 1].append(u - 1)

        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for nighbour in tree[node]:
                if nighbour == parent:
                    continue

                dfs(nighbour, node, d + 1)

        dfs(0, -1, 0)

        for j in range(1, LOG):
            for node in range(n):
                prev_jump = up[node][j - 1]
                if prev_jump != -1:
                    up[node][j] = up[prev_jump][j - 1]

        def get_lca(u, v):
            if depth[u] > depth[v]:
                u, v = v, u

            diff = depth[v] - depth[u]

            for j in range(LOG):
                if (diff >> j) & 1:
                    v = up[v][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        ans = []

        for u, v in queries:
            u, v = u - 1, v - 1
            if u == v:
                ans.append(0)
                continue
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - (2 * depth[lca])
            cost = pow(2, (dist - 1), MOD)
            ans.append(cost)

        return ans
