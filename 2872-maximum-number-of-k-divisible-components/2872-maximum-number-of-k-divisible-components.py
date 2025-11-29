class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        def dfs(node, parent):
            nonlocal ans
            total = 0
            for nighbour in graph[node]:
                if nighbour == parent:
                    continue
                total += dfs(nighbour, node)

            total += values[node]
            total %= k

            if total == 0:
                ans += 1

            return total

        dfs(0, -1)
        return ans
