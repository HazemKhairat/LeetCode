class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        h1, h2, w1, w2 = 0, 0,0,0
        ok = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    h1 = i
                    ok = True
                    break
            if ok:
                ok = not ok
                break

        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 1:
                    h2 = i + 1
                    ok = True
                    break
            if ok:
                ok = not ok
                break
        
        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    w1 = j
                    ok = True
                    break
            if ok:
                ok = not ok
                break

        for j in range(m - 1, -1, -1):
            for i in range(n):
                if grid[i][j] == 1:
                    w2 = j + 1
                    ok = True
                    break
            if ok:
                ok = not ok
                break
            

            
        return (w2 - w1) * (h2 - h1)
        
