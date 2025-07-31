class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        
        graph = [[] * n for _ in range(n)]
        res = -1

        @cache
        def dfs(node, l, score):
            nonlocal res
            if l == k and score < t:
                res = max(res, score)

            for nighbour, cost in graph[node]:
                dfs(nighbour, l + 1, score + cost)

            
        for edge in edges:
            u, v, w = edge
            graph[u].append((v, w))


        for i in range(n):
            dfs(i, 0, 0)

        return res