class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * m for i in range(n)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        vis = set()

        def top(r, c):
            res = 0
            for i in range(r - 1, -1, -1):
                if grid[i][c] == 2 or grid[i][c] == 1: break
                if (i, c) not in vis:
                    res += 1
                    vis.add((i, c))
            return res
        def buttom(r, c):
            res = 0
            for i in range(r + 1, n):
                if grid[i][c] == 2 or grid[i][c] == 1: break
                if (i, c) not in vis:
                    res += 1
                    vis.add((i, c))
            return res
        
        def left(r, c):
            res = 0
            for i in range(c - 1, -1, -1):
                if grid[r][i] == 2 or grid[r][i] == 1: break
                if (r, i) not in vis:
                    res += 1
                    vis.add((r, i))
            return res

        def right(r, c):
            res = 0
            for i in range(c + 1, m):
                if grid[r][i] == 2 or grid[r][i] == 1: break
                if (r, i) not in vis:
                    res += 1
                    vis.add((r, i))
            return res
        
        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans += 1 + left(r, c) + right(r, c) + top(r, c) + buttom(r, c)
                elif grid[r][c] == 2:
                    ans += 1
        return (n * m) - ans

        