class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        n = len(edges) + 1
        MOD = 10**9 + 7
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        def dfs(parent, node):
            
            max_depth = 0
            for nighbour in graph[node]:
                if parent == nighbour:
                    continue
                
                max_depth = max(max_depth, 1 + dfs(node, nighbour))
            
            return max_depth
        

        max_depth = dfs(-1, 1)

        ans = 2**(max_depth-1) % MOD
        return ans
        
