class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [-1 for _ in range(target + 1)]

        def solve(target):
            if target < 0:
                return 0
            if target == 0:
                return 1

            if dp[target] != -1:
                return dp[target]

            ans = 0
            for i in range(len(nums)):
                ans += solve(target - nums[i])

            dp[target] = ans
            return dp[target]

        return solve(target)
