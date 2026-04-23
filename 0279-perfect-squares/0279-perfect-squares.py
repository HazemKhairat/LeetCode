class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        for i in range(1, int(math.sqrt(n)) + 1):
            arr.append(i * i)
        
        arr = arr[::-1]

        dp = [[0 for _ in range(n + 1)] for _ in range(len(arr) + 1)]

        def solve(n, idx):
            if idx == len(arr) or n < 0:
                return inf

            if n - arr[idx] == 0:
                return 1

            
            if dp[idx][n]:
                return dp[idx][n]

            take = skip = 0
            take = 1 + solve(n - arr[idx], idx)
            skip = solve(n, idx + 1)

            dp[idx][n] = min(take, skip)
            return min(take, skip)

        return solve(n, 0)
