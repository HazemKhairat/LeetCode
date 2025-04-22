class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) + 5
        dp = [-1] * n 

        def solve(i, prev_index):
            if i == len(nums):
                return 0
            if dp[prev_index + 1] != -1:
                return dp[prev_index + 1]
            take, skip = 0, 0
            if prev_index < 0 or nums[i] > nums[prev_index]:
                take = 1 + solve(i + 1, i)
            skip = solve(i + 1, prev_index)
            dp[prev_index + 1] = max(take, skip)
            return dp[prev_index + 1]

        return solve(0, -1)
