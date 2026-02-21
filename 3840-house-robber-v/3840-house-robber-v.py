class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:

        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                dp[i + 1] = dp[i] + nums[i]
            else:
                dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[-1]
