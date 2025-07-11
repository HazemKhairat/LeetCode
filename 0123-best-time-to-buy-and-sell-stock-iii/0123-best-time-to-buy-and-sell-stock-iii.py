class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[[[ -1 for _ in range(3)] for _ in range(3)] for _ in range(2)] for _ in range(n)]

        def solve(index, Buy, b, s):
            if index == len(prices):
                return 0

            if memo[index][Buy][s][b] != -1:
                return memo[index][Buy][s][b]

            skip = buy = sell = 0
        
            if Buy and s:
                sell = prices[index] + solve(index + 1, False, b, s - 1)
            elif b:
                buy = -prices[index] + solve(index + 1, True, b - 1, s)
            
            skip = solve(index + 1, Buy, b, s)
            memo[index][Buy][s][b] = max(buy, sell, skip)
            return memo[index][Buy][s][b]
        
        return solve(0, False, 2, 2)
