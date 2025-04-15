class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    mat[i][j] += min(mat[i + 1][j], mat[i + 1][j - 1])
                elif j == 0:
                    mat[i][j] += min(mat[i + 1][j], mat[i + 1][j + 1])
                else:
                    mat[i][j] += min(
                        mat[i + 1][j], mat[i + 1][j + 1], mat[i + 1][j - 1]
                    )
        return min(mat[0])
