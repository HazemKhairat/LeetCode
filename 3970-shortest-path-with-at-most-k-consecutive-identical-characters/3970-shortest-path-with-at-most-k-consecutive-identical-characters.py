import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dis = [[inf] * (k + 1) for _ in range(n + 1)]

        pq = []  # w, node, c
        heapq.heappush(pq, (0, 0, 1))

        while pq:
            w, node, c = heapq.heappop(pq)

            if node == n - 1:
                return w

            for v, wi in graph[node]:
                next_cons = c + 1 if labels[node] == labels[v] else 1

                if next_cons > k:
                    continue

                if w + wi < dis[v][next_cons]:
                    dis[v][next_cons] = w + wi
                    heapq.heappush(pq, (wi + w, v, next_cons))

        return -1
