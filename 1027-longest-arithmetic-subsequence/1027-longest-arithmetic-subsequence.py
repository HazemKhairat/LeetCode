class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return 2
        ans = 2

        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])

        return ans
