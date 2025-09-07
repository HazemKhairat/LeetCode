class Solution:
    def minTimeToReach(self, mt: List[List[int]]) -> int:
        n, m = len(mt), len(mt[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        pq = [] # time, r, c, steps
        heapq.heappush(pq, [0, 0, 0, 0])
        vis = set()
        vis.add((0,0))
        
        def notValid(r, c):
            return r < 0 or c < 0 or r == n or c == m
            
        while pq:
            t, r, c, s = heapq.heappop(pq)
            if r == n - 1 and c == m - 1:
                return t
            
            alt = 1 if s % 2 == 0 else 2
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if notValid(nr, nc): continue
                if (nr, nc) in vis: continue
                vis.add((nr, nc))
                newT = max(t, mt[nr][nc]) + alt
                heapq.heappush(pq, [newT, nr, nc, s + 1])
        
        return 0
            




