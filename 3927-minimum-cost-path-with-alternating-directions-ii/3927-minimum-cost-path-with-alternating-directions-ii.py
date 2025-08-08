class Solution:
    def minCost(self, m: int, n: int, w: List[List[int]]) -> int:
        w[0][0] = 1
        w[-1][-1] = 0

        for r in range(m):
            for c in range(n):
                cost = (r + 1) * (c + 1)
                left = top = inf
                if c > 0: left = w[r][c - 1]
                if r > 0: top = w[r -1][c]
                if r == 0 and c == 0: continue
                w[r][c] += (min(left, top) + cost)
            
        return w[-1][-1]