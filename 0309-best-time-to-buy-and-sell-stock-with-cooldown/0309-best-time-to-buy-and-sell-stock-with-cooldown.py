class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def solve(index, isBuy, selled):
            if index == n:
                return 0
            key = (index, isBuy, selled)
            if key in memo:
                return memo[key]
            take = skip = sell = 0

            if selled:
                skip = solve(index + 1, False, False)
            elif isBuy == False:
                take = -prices[index] + solve(index + 1, True, False)
                skip = solve(index + 1, isBuy, selled)
            else:
                sell = prices[index] + solve(index + 1, False, True)
                skip = solve(index + 1, isBuy, selled)

            memo[key] = max(take, skip, sell)
            return memo[key]

        return solve(0, False, False)
