class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i > j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            skip = start = end = float("inf")
            if s[i] == s[j]:
                skip = solve(i + 1, j - 1)

            start = 1 + solve(i + 1, j)
            end = 1 + solve(i, j - 1)
            memo[i][j] = min(start, end, skip)

            return memo[i][j]

        return solve(0, n - 1)
