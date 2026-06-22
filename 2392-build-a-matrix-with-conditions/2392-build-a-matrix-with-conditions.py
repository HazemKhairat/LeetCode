class Solution:

    def topological_sort(self, adj, cells, di):
        k = len(cells)
        degree = [0] * (k + 1)

        for i in range(1, k):
            for node in adj[i]:
                degree[node] += 1

        q = deque()
        for i in range(1, k):
            if degree[i] == 0:
                q.append(i)

        processed = 0
        level = 0
        while q:
            first = q.popleft()
            cells[first][di] = level
            level += 1
            processed += 1
            for node in adj[first]:
                degree[node] -= 1
                if degree[node] == 0:

                    q.append(node)

        return processed != (k - 1)

    def buildMatrix(
        self, k: int, rows: List[List[int]], cols: List[List[int]]
    ) -> List[List[int]]:
        adj_row = [[] for _ in range(k + 1)]
        adj_col = [[] for _ in range(k + 1)]
        cells = [[-1, -1] for _ in range(k + 1)]
        ans = [[0] * k for _ in range(k)]

        for u, v in rows:
            adj_row[u].append(v)

        for u, v in cols:
            adj_col[u].append(v)

        has_cycle = self.topological_sort(adj_row, cells, 0) or self.topological_sort(
            adj_col, cells, 1
        )

        for i in range(1, len(cells)):
            r, c = cells[i][0], cells[i][1]
            ans[r][c] = i

        return ans if not has_cycle else []
