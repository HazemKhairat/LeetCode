class Solution:
    def strangePrinter(self, s: str) -> int:

        def removeDublicates(s):
            st = ""
            st += s[0]
            for i in range(1, len(s)):
                if s[i] != st[-1]:
                    st += s[i]
            return st

        s = removeDublicates(s)
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def solve(start, end):
            if start > end:
                return 0

            if memo[start][end] != -1:
                return memo[start][end]

            res = 1 + solve(start + 1, end)

            for i in range(start + 1, end + 1):
                if s[start] == s[i]:
                    res = min(res, solve(start, i - 1) + solve(i + 1, end))
            memo[start][end] = res
            return res

        return solve(0, len(s) - 1)
