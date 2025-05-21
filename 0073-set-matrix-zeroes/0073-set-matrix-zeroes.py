class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m, n = len(mat), len(mat[0])
        vis = [[0] * n for _ in range(m)]

        def top(i, j):
            while i >= 0:
                if mat[i][j] == 0:
                    i -= 1
                    continue
                mat[i][j] = 0
                vis[i][j] = 1
                i -= 1
            return

        def down(i, j):
            while i < m:
                if mat[i][j] == 0:
                    i += 1
                    continue
                mat[i][j] = 0
                vis[i][j] = 1
                i += 1
            return

        def left(i, j):
            while j >= 0:
                if mat[i][j] == 0:
                    j -= 1
                    continue
                mat[i][j] = 0
                vis[i][j] = 1
                j -= 1
            return

        def right(i, j):
            while(j < n):
                if mat[i][j] == 0:
                    j += 1
                    continue
                mat[i][j] = 0
                vis[i][j] = 1
                j += 1
            return
        
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0 and not vis[i][j]:
                    top(i, j)
                    down(i, j)
                    left(i, j)
                    right(i, j)



       
        return mat
