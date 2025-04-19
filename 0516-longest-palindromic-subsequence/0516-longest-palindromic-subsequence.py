class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for _ in range(1009)] for _ in range(1009)]

        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            if s[i] == s[j]:
                memo[i][j] = 2 + dfs(i + 1, j - 1)
            else:
                memo[i][j] = max(dfs(i + 1, j), dfs(i, j - 1))
            return memo[i][j]

        return dfs(0, len(s) - 1)
