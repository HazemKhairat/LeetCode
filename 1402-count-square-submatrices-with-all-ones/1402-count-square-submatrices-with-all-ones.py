class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 0:
                    continue
                mat[i][j] += min(mat[i - 1][j], mat[i][j - 1], mat[i - 1][j - 1])
        
        ans = 0
        for i in range(0, m):
            for j in range(0, n):
                ans += mat[i][j]

        return ans