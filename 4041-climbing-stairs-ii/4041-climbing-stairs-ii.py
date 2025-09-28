class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        dp = [inf] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            for step in range(1, 4):
                i = j - step
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + costs[j] + (j - i) ** 2)

        return dp[n]
