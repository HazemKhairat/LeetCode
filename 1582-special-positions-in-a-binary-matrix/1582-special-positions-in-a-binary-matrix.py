class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        n, m = len(mat), len(mat[0])

        def solve(r, c):
            ones = 0
            for i in range(n):
                if mat[i][c] == 1:
                    ones += 1
            for i in range(m):
                if mat[r][i] == 1:
                    ones += 1

            return ones == 2

        ans = 0
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    ans += solve(r, c)

        return ans
