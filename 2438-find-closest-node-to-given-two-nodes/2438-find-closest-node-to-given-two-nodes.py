class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]

        for i, edge in enumerate(edges):
            graph[i].append(edge)

        arr1 = set()
        arr2 = set()
        arr1.add(node1)
        arr2.add(node2)
        dis1 = [float("inf")] * n
        dis1[node1] = 0
        dis2 = [float("inf")] * n
        dis2[node2] = 0
        vis = set()
        vis.add(node1)
        vis.add(-1)

        def dfs(node, dis, arr, l):
            for nighbour in graph[node]:
                if nighbour in vis:
                    continue
                vis.add(nighbour)
                arr.add(nighbour)
                dfs(nighbour, dis, arr, l + 1)
                dis[nighbour] = l

        dfs(node1, dis1, arr1, 1)
        vis.clear()
        vis.add(node2)
        vis.add(-1)
        dfs(node2, dis2, arr2, 1)

        common = []
        for item in arr1:
            if item in arr2:
                common.append(item)

        print(common)

        tmp = float("inf")
        res = -1
        for item in common:
            maxi = max(dis1[item], dis2[item])
            if maxi < tmp:
                res = item
                tmp = min(maxi, tmp)

        return res
