class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1])

        return dp[-1]
