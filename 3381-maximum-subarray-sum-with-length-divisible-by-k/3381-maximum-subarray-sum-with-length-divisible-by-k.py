class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]

        dp = [-inf] * n
        for i in range(k, n):
            curr = nums[i] - nums[i - k]
            dp[i] = max(curr, curr + dp[i - k])

        return max(dp)
