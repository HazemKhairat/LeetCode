class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:

        dp = [-1 for _ in range(len(q))]

        def solve(idx):
            if idx >= len(q):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            take = skip = 0
            take = q[idx][0] + solve(idx + 1 + q[idx][1])
            skip = solve(idx + 1)

            dp[idx] = max(take, skip)
            return dp[idx]

        return solve(0)
