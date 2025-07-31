class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        Sum = 0
        def dfs(i, j):
            nonlocal Sum
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j]:
                return
            
            if grid[i][j]:
                Sum += grid[i][j]
                grid[i][j] = 0
                
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                Sum = 0
                dfs(i, j)
                if Sum % k == 0:
                    res += 1
                

        
        return res