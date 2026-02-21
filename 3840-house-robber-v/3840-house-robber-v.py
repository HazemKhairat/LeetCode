class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:

        n = len(nums)
        dp0, dp1 = 0, nums[0]

        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                dp0, dp1 = dp1, dp1 + nums[i]
            else:
                dp0, dp1 = dp1, max(dp1, dp0 + nums[i])

        return dp1
