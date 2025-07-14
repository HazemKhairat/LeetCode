class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for i in range(m)]
                
        def allVisited(visit):
            
            for i in range(len(visit)):
                for j in range(len(visit[0])):
                    if grid[i][j] == -1 or grid[i][j] == 2:
                        visit[i][j] = 1
                    if visit[i][j] == 0:
                        return False
            print(visit)
            
            return True

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == -1 or visit[i][j]:
                return 0
            if grid[i][j] == 2 and allVisited(visit):
                visit[i][j] = 0 # backtrack from making 2 cell visited
                return 1
            
            visit[i][j] = 1
            left = dfs(i, j -1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            visit[i][j] = 0

            return left + right + up + down
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = dfs(i, j)
                
        return res
            