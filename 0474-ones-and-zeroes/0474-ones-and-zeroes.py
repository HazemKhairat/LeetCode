class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        ones = [0] * len(strs)
        zeros = [0] * len(strs)

        for idx, st in enumerate(strs):
            for digit in st:
                if digit == "0":
                    zeros[idx] += 1
                else:
                    ones[idx] += 1

        # print(ones)
        # print(zeros)

        dp = [
            [[-1 for _ in range(len(strs) + 1)] for _ in range(n + 10)]
            for _ in range(m + 10)
        ]

        def solve(m, n, idx):
            if idx == len(strs):
                return 0

            if dp[m][n][idx] != -1:
                return dp[m][n][idx]

            take = skip = 0
            if m - zeros[idx] >= 0 and n - ones[idx] >= 0:
                take = 1 + solve(m - zeros[idx], n - ones[idx], idx + 1)

            skip = solve(m, n, idx + 1)
            dp[m][n][idx] = max(take, skip)
            return dp[m][n][idx]

        return solve(m, n, 0)
