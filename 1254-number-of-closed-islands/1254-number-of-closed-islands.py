class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += self.bfs(i, j, m, n, grid)

        return count

    def bfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]]) -> bool:
        q = deque([(x, y)])
        is_closed = True
        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        while q:
            x, y = q.popleft()
            grid[x][y] = 1
            for i in range(4):
                r, c = x + dirx[i], y + diry[i]
                if r < 0 or r >= m or c < 0 or c >= n:
                    # (x, y) is a boundary cell.
                    is_closed = False
                elif grid[r][c] == 0:
                    q.append((r, c))

        return is_closed
