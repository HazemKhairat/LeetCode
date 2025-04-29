class Solution:

    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n = max(len(t1), len(t2))
        memo = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == len(t1) or j == len(t2):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            ok = tryLeft = tryRight = 0

            if t1[i] == t2[j]:
                ok = 1 + solve(i + 1, j + 1)
            tryLeft = solve(i + 1, j)
            tryRight = solve(i, j + 1)

            memo[i][j] = max(ok, tryLeft, tryRight)
            return memo[i][j]

        return solve(0, 0)
