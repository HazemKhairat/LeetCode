class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[None for _ in range(amount + 1)] for _ in range(len(coins))]

        def solve(idx, amount):
            if idx == len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1

            if dp[idx][amount] != None:
                return dp[idx][amount]

            take = skip = 0
            take = solve(idx, amount - coins[idx])
            skip = solve(idx + 1, amount)

            dp[idx][amount] = take + skip
            return take + skip

        return solve(0, amount)