class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        maxArea = 0
        n, m = len(mat), len(mat[0])
        for i in range(0, n):
            maxArea = max(maxArea, int(mat[i][0]))

        for i in range(0, m):
            maxArea = max(maxArea, int(mat[0][i]))

        for i in range(1, n):
            for j in range(1, m):
                if int(mat[i][j]):
                    mat[i][j] = str(
                        min(
                            int(mat[i][j - 1]),
                            int(mat[i - 1][j]),
                            int(mat[i - 1][j - 1]),
                        )
                        + 1
                    )
                    maxArea = max(maxArea, int(mat[i][j]))

        return maxArea * maxArea
