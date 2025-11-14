class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:

        mat = [[0 for _ in range(n + 1)] for _ in range(n)]

        for i in range(len(q)):
            for r in range(q[i][0], q[i][2] + 1):
                c1, c2 = q[i][1], q[i][3]
                mat[r][c1] += 1
                mat[r][c2 + 1] -= 1

        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]

        mat = [row[:-1] for row in mat]
        return mat
