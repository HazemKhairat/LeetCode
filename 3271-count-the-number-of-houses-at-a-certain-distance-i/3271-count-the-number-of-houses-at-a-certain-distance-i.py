class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = [[] for _ in range(n + 1)]
        for i in range(1, n):
            graph[i].append(i + 1)
            graph[i + 1].append(i)
        
        if x != y:
            graph[x].append(y)
            graph[y].append(x)
            
        ans = [0] * n

        def bfs(root):
            vis = [False] * (n + 1)
            q = deque()
            q.append(root)
            vis[root] = True
            level = 0
            while q:
                size = len(q)
                while size:
                    node = q.popleft()
                    for nighbour in graph[node]:
                        if vis[nighbour]: continue
                        vis[nighbour] = True
                        q.append(nighbour) 
                    size -= 1

                ans[level] += len(q)
                level += 1

        for i in range(1, n + 1):
            bfs(i)
        
        return ans
