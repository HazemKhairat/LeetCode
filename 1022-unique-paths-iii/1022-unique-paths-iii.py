class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        total = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total += 1
                elif grid[i][j] == 1:
                    start_x, start_y = i, j
        

        def dfs(i, j):
            nonlocal total
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] < 0:
                return 0

            if grid[i][j] == 2:
                return 1 if total == 0 else 0
            
            grid[i][j] = -2
            total -= 1
            path = ( dfs(i, j -1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j) )
            grid[i][j] = 0
            total += 1

            return path
        
       
                
        return dfs(start_x, start_y)
            