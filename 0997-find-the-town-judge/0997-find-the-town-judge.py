class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:     

        # create the graph to trace property 1
        graph = {}
        for i in range(1, n + 1): graph[i] = [i]

        # create counter to trace property 2
        cnt = [1] * (n + 1)

        # Initiate the graph and counter
        for u, v in trust:
            graph[u].append(v)
            cnt[v] += 1

        ans = -1
        ok = 0
        for i in range(1, n + 1):
            # town judge condition
            if cnt[i] == n and len(graph[i]) == 1:
                ans = i
                ok += 1
        
        # Only 1 town judge else -1
        return ans if ok == 1 else -1




