class Solution:
    def champagneTower(self, p: int, qr: int, qg: int) -> float:
        dp = [[0] * (qr + 2) for _ in range(qr + 2)]
        dp[0][0] = p

        for r in range(qr + 1):
            for c in range(qr + 1):
                if dp[r][c] > 1:
                    excess = (dp[r][c] - 1.0) / 2.0
                    dp[r][c] = 1
                    dp[r + 1][c] += excess
                    dp[r + 1][c + 1] += excess

        return dp[qr][qg]
