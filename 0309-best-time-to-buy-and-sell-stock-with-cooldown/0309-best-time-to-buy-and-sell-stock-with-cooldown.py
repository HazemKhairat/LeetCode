class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [float("inf")] * n

        @cache
        def solve(index, isBuy, selled):
            if index == n:
                return 0

            # if memo[index] != float('inf'):
            #     return memo[index]
            take = skip = sell = 0

            if selled:
                skip = solve(index + 1, False, False)
            elif isBuy == False:
                take = -prices[index] + solve(index + 1, True, False)
                skip = solve(index + 1, isBuy, selled)
            else:
                sell = prices[index] + solve(index + 1, False, True)
                skip = solve(index + 1, isBuy, selled)

            # memo[index] = max(take, skip, sell)
            return max(take, skip, sell)

        return solve(0, False, False)
