class Solution:
    def minimumFlips(
        self, n: int, edges: List[List[int]], start: str, target: str
    ) -> List[int]:
        has_issue = [start[idx] != target[idx] for idx in range(n)]
        if has_issue.count(True) % 2 == 1:
            return [-1]

        ans = []
        graph = [[] for _ in range(n)]
        degree = [0] * n

        for idx, (u, v) in enumerate(edges):
            graph[u].append((v, idx))
            graph[v].append((u, idx))
            degree[u] += 1
            degree[v] += 1

        q = deque([node for node in range(n) if degree[node] == 1])

        while q:
            node = q.popleft()
            degree[node] -= 1

            for nighbour, idx in graph[node]:
                if not degree[nighbour]:
                    continue
                if has_issue[node]:
                    ans.append(idx)
                    has_issue[node] = False
                    has_issue[nighbour] = not has_issue[nighbour]

                degree[nighbour] -= 1
                if degree[nighbour] == 1:
                    q.append(nighbour)

        return sorted(ans)
