class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0

        def dfs(curr, parent):
            nonlocal count
            total = 0
            for nei in graph[curr]:
                if nei == parent:
                    continue
                total += dfs(nei, curr)

            total += values[curr]
            total %= k

            if total == 0:
                count += 1

            return total

        dfs(0, -1)
        return count
