class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        ans = 0
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        groups = defaultdict(list)
        for i in range(len(group)):
            groups[group[i]].append(i)
        
        for nodes in groups.values():
            m = len(nodes)
            is_in_same_group = [0] * n
            for node in nodes:
                is_in_same_group[node] = 1

            def dfs(node, parent):
                nonlocal ans
                cnt = is_in_same_group[node]

                for nighbour in graph[node]:
                    if nighbour == parent:
                        continue

                    c = dfs(nighbour, node)
                    ans += c * (m - c)
                    cnt += c

                return cnt
            
            dfs(nodes[0], -1)


        return ans