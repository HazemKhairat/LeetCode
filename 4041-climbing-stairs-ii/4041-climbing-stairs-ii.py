class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        costs = [0] + costs
        n = len(costs)
        dp = [inf] * n
        dp[0] = 0

        for j in range(1, n):
            for s in range(1, 4):
                i = j - s
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + costs[j] + (j - i) ** 2)

        return dp[n - 1]