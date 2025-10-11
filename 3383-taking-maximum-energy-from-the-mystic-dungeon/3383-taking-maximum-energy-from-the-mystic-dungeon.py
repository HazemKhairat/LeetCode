class Solution:
    def maximumEnergy(self, dp: List[int], k: int) -> int:
        n = len(dp)
        ans = dp[-1]

        for i in range(k, n):
            dp[i] = max(dp[i], dp[i] + dp[i - k])

        for i in range(n - k, n):
            ans = max(ans, dp[i])

        return ans
