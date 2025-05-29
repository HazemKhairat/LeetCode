class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1), len(edges2)

        tree1 = [[] for _ in range(n + 1)]
        tree2 = [[] for _ in range(m + 1)]

        for edge in edges1:
            u,v = edge
            tree1[u].append(v)
            tree1[v].append(u)

        for edge in edges2:
            u,v = edge
            tree2[u].append(v)
            tree2[v].append(u)

        # tree1 BFS
        q = deque()
        q.append(0)
        colors = [False] * (n + 1)
        colors[0] = True
        vis = [False] * (n + 1)
        vis[0] = True

        while q:
            node = q.popleft()
            for nighbour in tree1[node]:
                if not vis[nighbour]:
                    colors[nighbour] = not colors[node]
                    q.append(nighbour)
                    vis[nighbour] = True
        
        even = sum(colors)
        odd = len(colors) - even

        # tree2 BFS

        q.append(0)
        colors2 = [False] * (m + 1)
        colors2[0] = True
        vis = [False] * (m + 1)
        vis[0] = True

        while q:
            node = q.popleft()
            for nighbour in tree2[node]:
                if not vis[nighbour]:
                    colors2[nighbour] = not colors2[node]
                    q.append(nighbour)
                    vis[nighbour] = True
                
        temp = sum(colors2)
        maxi = max(temp, m + 1 - temp)

        res = [0] * (n + 1)
        for i in range(n + 1):
            if colors[i]:
                res[i] = even + maxi
            else:
                res[i] = odd + maxi
            
        return res