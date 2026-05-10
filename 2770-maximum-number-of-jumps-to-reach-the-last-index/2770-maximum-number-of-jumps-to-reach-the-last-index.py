class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        n = len(nums)
        dp = [-inf] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (-1 * target) <= nums[j] - nums[i] <= target:
                    # print(nums[i])
                    # print(nums[j])
                    dp[j] = max(dp[j], dp[i] + 1)
                    # print(dp)

        return dp[-1] if dp[-1] != -inf else -1
