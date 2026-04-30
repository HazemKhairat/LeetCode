class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1 for _ in range(amount + 10)] for _ in range(len(coins) + 1)]

        def solve(idx, amount):
            if idx == len(coins):
                return inf

            if amount == 0:
                return 0

            if dp[idx][amount] != -1:
                return dp[idx][amount]

            take = skip = inf
            if amount - coins[idx] >= 0:
                take = 1 + solve(idx, amount - coins[idx])

            skip = solve(idx + 1, amount)
            dp[idx][amount] = min(take, skip)
            return dp[idx][amount]

        ans = solve(0, amount)
        return ans if ans != inf else -1
