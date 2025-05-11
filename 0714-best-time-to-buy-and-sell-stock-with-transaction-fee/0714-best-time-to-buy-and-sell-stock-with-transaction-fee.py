class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        memo = {}

        def solve(index, isBuy, isSell):
            if index == n:
                return 0
            key = (index, isBuy, isSell)
            if key in memo:
                return memo[key]

            buy = sell = skip = 0

            if not isBuy:
                buy = (-1 * prices[index]) + solve(index + 1, True, False)
            elif not isSell:
                sell = (-1 * fee) + prices[index] + solve(index + 1, False, True)

            skip = solve(index + 1, isBuy, isSell)

            memo[key] = max(buy, sell, skip)
            return memo[key]

        return solve(0, False, False)
