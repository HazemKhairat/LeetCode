class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        # 0  1 2 3 4 5  6  7
        # 10 9 2 5 3 7 101 18
        #  1 1 1 2 2 3  4   4

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
